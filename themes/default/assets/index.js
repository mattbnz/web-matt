import * as metrics from '@mattbnz/metrics';
import * as params from '@params';

metrics.SetupMetrics(params.MetricsHost, 60);

window.addEventListener("load", (e) => {
    Array.from(document.getElementsByClassName("mb-subButton")).forEach((b) => {
        b.addEventListener("click", subscribe);
    });
});

async function postData(url = '', data = {}) {
    try {
        const response = await fetch(url, {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify(data)
        });
        return response;
    } catch {
        return {ok: false}
    }
}

function isvalid(e) {
    return /(.+)@(.+){2,}\.(.+){2,}/.test(e);
}

function subscribe(evt) {
    var formID = evt.target.dataset.formid;

    var b = document.getElementById("subButton-" + formID);
    var e = document.getElementById("subEmail-" + formID);
    var m = document.getElementById("subError-" + formID);
    var w = document.getElementById("subWrapper-" + formID);
    var s = document.getElementById("subSuccess-" + formID);
    if (!isvalid(e.value)) {
      m.innerText = "Invalid email!";
      m.classList.add("text-pink-800");
      e.classList.add("text-pink-800");
      return;
    }
    m.classList.remove("text-pink-800");
    e.classList.remove("text-pink-800");
    e.disabled = true;
    b.disabled = true;
    b.value = "Subscribing...";
    postData(params.SubscribeUrl, {email: e.value}).then((r) => {
      if (r.ok) {
        w.classList.add("hidden");
        m.classList.add("hidden");
        s.classList.remove("hidden");
      } else {
        m.classList.add("text-pink-800");
        b.value = "Failed!";
        m.innerText = "Uh oh! Something went wrong, email hi@mattb.nz please!"
      }
    });
}