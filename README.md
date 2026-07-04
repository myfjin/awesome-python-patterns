# awesome-python-patterns

**Not a link list, and not idiom snippets — 99 runnable, run-gated, stdlib-only Python patterns.**

Every file in this repository:

- **runs** — `python3 patterns/<category>/<pattern>.py` executes a working demo/self-test, standard library only, no pip install, no network;
- **passed a run-gate** — executed end-to-end, per-pattern, logged (see [`gate_logs/`](gate_logs/)) before it was allowed in;
- **is real implementation** — data structures, distributed-systems machinery, resilience patterns — not toy pseudocode.

## Quick start

```bash
git clone https://github.com/myfjin/awesome-python-patterns
cd awesome-python-patterns
python3 patterns/distributed/raft_consensus.py     # watch a Raft cluster elect a leader
python3 patterns/data_structures/red_black_tree.py # watch a red-black tree stay balanced
python3 tools/run_gate.py                          # run the whole gate yourself
```

## The patterns

### Data Structures (18)

| Pattern | What it is |
|---|---|
| [`avl_tree`](patterns/data_structures/avl_tree.py) | AVL Tree Implementation |
| [`binary_indexed_tree`](patterns/data_structures/binary_indexed_tree.py) | Binary Indexed Tree |
| [`bloom_filter`](patterns/data_structures/bloom_filter.py) | Bloom Filter |
| [`fenwick_tree`](patterns/data_structures/fenwick_tree.py) | Fenwick Tree (Binary Indexed Tree) implementation with comprehensive functionality. |
| [`interval_tree`](patterns/data_structures/interval_tree.py) | Interval Tree |
| [`kd_tree`](patterns/data_structures/kd_tree.py) | A complete k-d tree implementation for 2D points with insert, nearest neighbor, |
| [`merkle_tree`](patterns/data_structures/merkle_tree.py) | A simple Merkle tree implementation using SHA-256 hashing. |
| [`ordered_map`](patterns/data_structures/ordered_map.py) | Ordered Map |
| [`persistent_deque`](patterns/data_structures/persistent_deque.py) | Persistent Deque |
| [`priority_task_scheduler`](patterns/data_structures/priority_task_scheduler.py) | Priority Queue Scheduler Module |
| [`radix_tree`](patterns/data_structures/radix_tree.py) | Radix Tree |
| [`red_black_tree`](patterns/data_structures/red_black_tree.py) | Red Black Tree |
| [`segment_tree`](patterns/data_structures/segment_tree.py) | Segment Tree |
| [`skip_list`](patterns/data_structures/skip_list.py) | Skip List |
| [`suffix_array`](patterns/data_structures/suffix_array.py) | Suffix Array |
| [`treap`](patterns/data_structures/treap.py) | Treap |
| [`trie`](patterns/data_structures/trie.py) | Trie (Prefix Tree) implementation with autocomplete functionality. |
| [`union_find`](patterns/data_structures/union_find.py) | Union Find |
### Monitoring & Observability (12)

| Pattern | What it is |
|---|---|
| [`alert_manager`](patterns/monitoring/alert_manager.py) | Alert Manager |
| [`event_logger`](patterns/monitoring/event_logger.py) | Structured event logger with rotation capabilities. |
| [`log_pattern_matcher`](patterns/monitoring/log_pattern_matcher.py) | Log Pattern Matcher |
| [`metric_aggregation_engine`](patterns/monitoring/metric_aggregation_engine.py) | Metric Aggregation Engine |
| [`metric_aggregator`](patterns/monitoring/metric_aggregator.py) | Metric aggregator with tags for counters, gauges, and histograms. |
| [`metrics_formatter`](patterns/monitoring/metrics_formatter.py) | Metrics Formatter |
| [`time_series_db`](patterns/monitoring/time_series_db.py) | In-memory time-series database module with support for insertion, querying, |
| [`timer_stack`](patterns/monitoring/timer_stack.py) | Timer Stack |
| [`trace_collector`](patterns/monitoring/trace_collector.py) | Trace Collector |
| [`trace_sampler`](patterns/monitoring/trace_sampler.py) | Distributed Tracing Sampler Module |
| [`trace_span_collector`](patterns/monitoring/trace_span_collector.py) | Distributed Tracing Span Collector Module |
| [`window_sampler`](patterns/monitoring/window_sampler.py) | Anomaly Detection Sampler Module |
### Performance (11)

| Pattern | What it is |
|---|---|
| [`batch_controller`](patterns/performance/batch_controller.py) | Adaptive Batch Size Controller |
| [`budget_allocator`](patterns/performance/budget_allocator.py) | Request Collapser Module |
| [`free_list_allocator`](patterns/performance/free_list_allocator.py) | Free List Allocator |
| [`hyperloglog`](patterns/performance/hyperloglog.py) | HyperLogLog probabilistic cardinality estimator implementation. |
| [`job_scheduler`](patterns/performance/job_scheduler.py) | A simple job scheduler with cron-like expressions. |
| [`lru_cache`](patterns/performance/lru_cache.py) | Lru Cache |
| [`object_pool_allocator`](patterns/performance/object_pool_allocator.py) | Object Pool Allocator |
| [`resource_budget_allocator`](patterns/performance/resource_budget_allocator.py) | Resource Budget Allocator Module |
| [`rw_lock`](patterns/performance/rw_lock.py) | Rw Lock |
| [`token_bucket`](patterns/performance/token_bucket.py) | Token Bucket |
| [`work_stealing_queue`](patterns/performance/work_stealing_queue.py) | Work-Stealing Queue Implementation |
### Distributed Systems (9)

| Pattern | What it is |
|---|---|
| [`consistent_hash_ring`](patterns/distributed/consistent_hash_ring.py) | Consistent Hash Ring Implementation |
| [`crdt_sets`](patterns/distributed/crdt_sets.py) | CRDT Sets Implementation |
| [`distributed_lock_manager`](patterns/distributed/distributed_lock_manager.py) | Distributed Lock Manager |
| [`g_counter_crdt`](patterns/distributed/g_counter_crdt.py) | Distributed Counter Implementation |
| [`gossip_protocol`](patterns/distributed/gossip_protocol.py) | Gossip Protocol Membership List Implementation |
| [`quorum_consensus`](patterns/distributed/quorum_consensus.py) | Quorum consensus simulator module. |
| [`raft_consensus`](patterns/distributed/raft_consensus.py) | Raft Consensus Algorithm Implementation |
| [`service_registry`](patterns/distributed/service_registry.py) | Service Registry |
| [`vector_clock`](patterns/distributed/vector_clock.py) | Vector Clock implementation for detecting causal relationships between events |
### Networking (9)

| Pattern | What it is |
|---|---|
| [`connection_pool`](patterns/networking/connection_pool.py) | Connection Manager with Pooling |
| [`connection_pool_health_checks`](patterns/networking/connection_pool_health_checks.py) | Connection Pool with Health Checks Module |
| [`dns_cache`](patterns/networking/dns_cache.py) | Dns Cache |
| [`http_retry_client`](patterns/networking/http_retry_client.py) | HTTP Client with Retry, Backoff, and Circuit Breaker Support |
| [`http_router`](patterns/networking/http_router.py) | HTTP Request Multiplexer Module |
| [`packet_parser`](patterns/networking/packet_parser.py) | Packet Parser |
| [`rate_limiter`](patterns/networking/rate_limiter.py) | Rate Limiter |
| [`rtt_estimator`](patterns/networking/rtt_estimator.py) | Round-trip time estimator module with EWMA smoothing and timeout calculation. |
| [`url_router`](patterns/networking/url_router.py) | Url Router |
### Algorithms & Reasoning (9)

| Pattern | What it is |
|---|---|
| [`astar_pathfinding`](patterns/reasoning/astar_pathfinding.py) | A* Pathfinding Algorithm Implementation |
| [`bayesian_network`](patterns/reasoning/bayesian_network.py) | Bayesian Belief Network Implementation |
| [`csp_solver`](patterns/reasoning/csp_solver.py) | Constraint Satisfaction Problem (CSP) Solver Module |
| [`decision_tree`](patterns/reasoning/decision_tree.py) | Simple Decision Tree Classifier |
| [`dependency_graph`](patterns/reasoning/dependency_graph.py) | Dependency Graph Resolver - Topological Sort Implementation |
| [`expression_evaluator`](patterns/reasoning/expression_evaluator.py) | Simple Expression Evaluator with Variables |
| [`minimax_game_search`](patterns/reasoning/minimax_game_search.py) | A complete minimax game solver with alpha-beta pruning and depth limiting. |
| [`rule_engine`](patterns/reasoning/rule_engine.py) | Rule-based inference engine with forward chaining and conflict resolution. |
| [`sat_solver`](patterns/reasoning/sat_solver.py) | Sat Solver |
### I/O & Parsing (8)

| Pattern | What it is |
|---|---|
| [`arg_parser`](patterns/io/arg_parser.py) | Arg Parser |
| [`chunked_reader`](patterns/io/chunked_reader.py) | Line-delimited file parser with chunked reads. |
| [`csv_to_json`](patterns/io/csv_to_json.py) | CSV to JSON converter module with type inference, nested key support, and streaming. |
| [`csv_validator`](patterns/io/csv_validator.py) | CSV Validator and Transformer Module |
| [`diff_engine`](patterns/io/diff_engine.py) | A simple diff engine for text comparison. |
| [`ini_parser`](patterns/io/ini_parser.py) | Simple INI file parser module. |
| [`log_parser`](patterns/io/log_parser.py) | JSON Schema Validator Module |
| [`template_engine`](patterns/io/template_engine.py) | Template Engine |
### Architecture (7)

| Pattern | What it is |
|---|---|
| [`cqrs_bus`](patterns/architecture/cqrs_bus.py) | Simple CQRS Command/Query Splitter Module |
| [`event_bus`](patterns/architecture/event_bus.py) | Event Bus with Typed Channels |
| [`event_sourcing_store`](patterns/architecture/event_sourcing_store.py) | Event Sourcing Store Implementation |
| [`message_encoder`](patterns/architecture/message_encoder.py) | Message Format Encoder/Decoder Module |
| [`plugin_registry`](patterns/architecture/plugin_registry.py) | Plugin registry with lazy loading, dependency management, and entry point discovery. |
| [`saga_coordinator`](patterns/architecture/saga_coordinator.py) | Saga Pattern Coordinator Module |
| [`state_machine`](patterns/architecture/state_machine.py) | Simple State Machine Engine |
### Async & Concurrency (5)

| Pattern | What it is |
|---|---|
| [`async_task_queue`](patterns/async/async_task_queue.py) | Async Task Queue with Priority and Retries |
| [`cancellable_task_group`](patterns/async/cancellable_task_group.py) | Async task group implementation with cancellation support. |
| [`priority_queue_scheduler`](patterns/async/priority_queue_scheduler.py) | Priority Queue with Deadline Scheduling Module |
| [`pubsub_broker`](patterns/async/pubsub_broker.py) | A simple pub-sub message broker implementation with wildcard topic matching. |
| [`reactive_signals`](patterns/async/reactive_signals.py) | Reactive Signals |
### Resilience (4)

| Pattern | What it is |
|---|---|
| [`bulkhead_isolator`](patterns/resilience/bulkhead_isolator.py) | Bulkhead Pattern Isolator Module |
| [`circuit_breaker`](patterns/resilience/circuit_breaker.py) | Circuit Breaker |
| [`dead_letter_queue`](patterns/resilience/dead_letter_queue.py) | Dead Letter Queue Handler Module |
| [`timeout_guard`](patterns/resilience/timeout_guard.py) | Timeout Guard |
### Persistence (3)

| Pattern | What it is |
|---|---|
| [`lsm_tree`](patterns/persistence/lsm_tree.py) | LSM-Tree Engine Implementation |
| [`segmented_wal`](patterns/persistence/segmented_wal.py) | Write-Ahead Log (WAL) implementation for durable transaction logging. |
| [`write_ahead_log`](patterns/persistence/write_ahead_log.py) | Write-Ahead Log (WAL) implementation for data durability and crash recovery. |
### Security (3)

| Pattern | What it is |
|---|---|
| [`capability_access`](patterns/security/capability_access.py) | Capability-Based Access Control System |
| [`hotp_totp`](patterns/security/hotp_totp.py) | Time-Based One-Time Password (TOTP) generator and validator. |
| [`secure_envelope`](patterns/security/secure_envelope.py) | Secure Envelope Module |
### Vision (1)

| Pattern | What it is |
|---|---|
| [`image_stats`](patterns/vision/image_stats.py) | Histogram-based image contrast stretcher module. |

## Quality bar

"Run-gated" means: we do not claim a pattern works — we run it, on the commit that ships it,
and keep the log. The gate script ships in this repo — one command lets you re-verify every claim yourself — and CI re-runs it on every push. If a pattern
is listed here, it executed cleanly with a 90-second timeout on the day of the commit.

## Provenance — stated honestly

These patterns were machine-harvested from **qwen3-coder:480b** (Apache 2.0, via Ollama cloud),
then human-curated: de-duplicated, categorized, policy-checked (stdlib-only), defect-fixed, and
run-gated per file. `MANIFEST.json` maps every pattern to its harvest session and checksum.
We think the honest description of this collection is: AI-generated, human-verified.

## C++ twins (coming)

Each of these patterns is being converted to modern C++17 — compiled and self-tested on
macOS (ARM64) and Linux (x86-64) — as a paid companion library. The free tier is this repo,
complete, forever. Watch [realityoptimizer.app](https://realityoptimizer.app) for the release.

## License

MIT — see [LICENSE](LICENSE).
