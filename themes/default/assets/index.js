import * as metrics from 'metrics';
import * as params from '@params';

metrics.SetupMetrics(params.MetricsHost, 60);