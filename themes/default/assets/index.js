import * as metrics from '@mattbnz/metrics';
import * as params from '@params';

metrics.SetupMetrics(params.MetricsHost, 60);