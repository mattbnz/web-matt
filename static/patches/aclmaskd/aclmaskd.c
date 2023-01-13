/*
 * Watch a directory or directories for changes and set the ACL mask to enable
 * all the ACLS. 
 *
 * Author:  Matt Brown <matt@mattb.net.nz>
 * Date:    2007-07-12
 *
 * Licensed under the GPLv2
 */
#define _GNU_SOURCE
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
extern int errno ;
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fam.h>
#include <unistd.h>
#include <signal.h>


struct monitordir {
    char *name;
    FAMRequest fr;
    struct monitordir *next;
};


static int endloop = 0;
void interrupt_handler(int sig) {
    endloop = 1;
    fprintf(stderr, "Caught signal!\n");
	return ;
}

int add_directory(FAMConnection *fc, struct monitordir **dirlist, char *name)
{
    struct monitordir *thisdir = NULL;
    thisdir = malloc(sizeof(struct monitordir));
    if (!thisdir) {
        fprintf(stderr, "Out of memory!\n");
        return 0;
    }
    thisdir->name = strdup(name);
    fprintf(stdout, "Registering directory %s\n", thisdir->name);
    if (FAMMonitorDirectory(fc, thisdir->name, &thisdir->fr, thisdir)) {
        fprintf(stderr, "Cannot monitor directory %s\n", thisdir->name);
        return 0;
    }
    thisdir->next = NULL;
    if (!*dirlist) {
        *dirlist = thisdir;
    } else {
        (*dirlist)->next = thisdir;
    }
    return 1;
}

char *mstr(unsigned int mode) {
    if (mode == S_IRGRP) {
        return "READ";
    } else if (mode == S_IWGRP) {
        return "WRITE";
    } else if (mode == S_IXGRP) {
        return "EXECUTE";
    } else {
        return "UNKNOWN";
    }
}
void check_set_mode(const char *dirname, struct stat *buf, unsigned int mode)
{
    if ((buf->st_mode & mode) != mode) {
        if (chmod(dirname, buf->st_mode|mode)!=0) {
            fprintf(stderr, "Could not set %s bit on %s: %s\n", mstr(mode),
                    dirname, strerror(errno));
            return;
        } else {
            fprintf(stdout, "Added %s bit on %s\n", mstr(mode), dirname);
        }
    }
}

void process_entry(FAMConnection *fc, struct monitordir **dirlist,
                   struct monitordir *dir, FAMEvent *fe)
{
    struct stat buf;
    char *fullname = NULL;
    struct monitordir *thisdir = *dirlist;
    int found=0;
    if (strncmp(dir->name, fe->filename, strlen(fe->filename))==0) {
        fullname = strdup(fe->filename);
        found=1;
    } else {
        if (asprintf(&fullname, "%s/%s", dir->name, fe->filename) < 0) {
            fprintf(stderr, "Unable to process %s!\n", fullname);
            return;
        }
    }
    if (stat(fullname, &buf)!=0) {
        fprintf(stderr, "Unable to stat %s!\n", fullname);
        free(fullname);
        return;
    }
    if (fe->code==FAMExists || fe->code==FAMCreated || fe->code==FAMChanged) {
        check_set_mode(fullname, &buf, S_IRGRP);
        check_set_mode(fullname, &buf, S_IWGRP);
        check_set_mode(fullname, &buf, S_IXGRP);
    }
    if (!S_ISDIR(buf.st_mode)) {
        // Exit now if we're not going to need to add/remove directories
        free(fullname);
        return;
    }
    if (!found && (fe->code==FAMExists || fe->code==FAMCreated)) {
        while (thisdir) {
            if (strncmp(thisdir->name, fullname, strlen(fullname))!=0) {
                thisdir = thisdir->next;
                continue;
            }
            found = 1;
            break;
            thisdir = thisdir->next;
        }
        if (!found) {
            add_directory(fc, dirlist, fullname);
        }
    } else if (fe->code==FAMDeleted) {
        // Find in the list
        struct monitordir *prev = *dirlist;
        while (thisdir) {
            if (strncmp(thisdir->name, fullname, strlen(fullname))==0) {
                // Cancel monitor
                FAMCancelMonitor(fc, &thisdir->fr);
                // Clean up
                free(thisdir->name);
                prev->next = thisdir->next;
                free(thisdir);
                fprintf(stdout, "Removed %s\n", fullname);
                break;
            }
            thisdir = thisdir->next;
        }
    }
    free(fullname);
}

int main(const int argc , const char **argv)
{

    signal(SIGINT, interrupt_handler);

    
	FAMConnection fc;
    if (FAMOpen(&fc)) {
        fprintf(stderr, "Unable to open connection to famd!\n");
        return 1;
    }
    
    struct monitordir *dirlist = NULL;

    for (int i=1; i < argc; ++i) {
        if (!add_directory(&fc, &dirlist, (char *)argv[i])) {
            return 1;
        }
    }

	if (!dirlist) {
        fprintf(stderr, "No directories specified!\n");
        return 1;
	}

    fd_set rfd;
	while (!endloop) {
        int rv=0;
        FD_ZERO(&rfd);
        FD_SET(fc.fd, &rfd);
        rv = select(fc.fd+1, &rfd, NULL, NULL, NULL);
        if (rv <= 0) {
            if (rv < 0) {
                fprintf(stderr, "Select exited with error: %s\n", 
                        strerror(errno));
            }
            continue;
        }
        while (FAMPending(&fc)) {
            FAMEvent fe;
            if (!FAMNextEvent(&fc, &fe)) {
                fprintf(stderr, "Failed to fetch next event\n");
                continue;
            }
            struct monitordir *thisdir = fe.userdata;
            if (fe.code==FAMChanged || fe.code==FAMCreated || 
                    fe.code==FAMMoved || fe.code==FAMExists) {
                fprintf(stdout, "%s/%s (%d)\n", thisdir->name, fe.filename, fe.code);
                process_entry(&fc, &dirlist, thisdir, &fe);
            }
        }
	}

    struct monitordir *thisdir = dirlist;
    while (thisdir) {
        struct monitordir *tmp = thisdir;
        FAMCancelMonitor(&fc, &thisdir->fr);
        free(thisdir->name);
        thisdir = thisdir->next;
        free(tmp);
    }

	FAMClose(&fc);
    return 0;
}

