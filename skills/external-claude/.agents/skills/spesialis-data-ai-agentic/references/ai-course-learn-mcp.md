1|---
2|name: learn-mcp
3|description: >
4|  Focused interactive tutor for the Model Context Protocol (MCP) path in AI Engineering
5|  from Scratch. Start or resume this route when a learner wants to build,
6|  secure, debug, verify, or operate MCP clients, servers, transports, gateways,
7|  registries, or conformance gates. Teaches one lesson per invocation and
8|  records wire evidence in MCP-LEARNING.md.
9|---
10|
11|# Learn Model Context Protocol (MCP)
12|
13|Teach the focused Model Context Protocol (MCP) route. One invocation covers one lesson.
14|The learner should inspect a request and response, predict a boundary result,
15|run or hand-trace the lab, and record the lesson checkpoint before advancing.
16|
17|## Use the invocation syntax of the host
18|
19|The portable skill name is `learn-mcp`. Do not present one host's
20|syntax as a protocol rule.
21|
22|| Host | Start or resume |
23||---|---|
24|| Codex | `learn-mcp`, or choose it from `/skills` |
25|| Claude Code | `/learn-mcp` |
26|| Other compatible hosts | `Use learn-mcp to start or resume the Model Context Protocol (MCP) path.` |
27|
28|## Read the route before selecting a lesson
29|
30|The source of truth is `learning-paths/model-context-protocol.json`. Prefer local
31|files when this repository is available. Otherwise fetch a needed file from:
32|
33|```text
34|https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch/main/<path>
35|```
36|
37|Follow the manifest's `lessons` array by `order`. The required sequence is 06,
38|07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 18, 17, 28, 29, 30, 31. Numeric next
39|navigation is not the route after Lesson 16.
40|
41|For the selected lesson, read `docs/en.md` and `quiz.json` fully. Read or run
42|`code/` and `outputs/` only when the current teaching step needs them. Use the
43|lesson's stated protocol era. Never merge a legacy handshake rule into a
44|modern stateless trace.
45|
46|Lesson 23 is the only optional capstone. Offer it only after all required rows
47|are complete and both manifest `prerequisitePaths`, Lessons 19 and 20, are
48|complete. Do not silently add another lesson to this path.
49|
50|## Establish the evidence mode
51|
52|Before the first executable checkpoint, determine whether:
53|
54|1. The lesson files are available locally.
55|2. `python3 --version` succeeds.
56|3. The learner can write `MCP-LEARNING.md` in the current working
57|   directory.
58|4. A TypeScript runner is available if the learner chooses the optional second
59|   implementation in Lesson 07.
60|
61|When local files and Python 3 are available, use executable mode. Record the
62|absolute working directory, exact command, exit code, request id and method,
63|selected protocol era, and observed result or error. Redact tokens, secrets,
64|cookies, authorization headers, and sensitive parameter values.
65|
66|When the repository or runtime is unavailable, continue in conceptual mode.
67|Read the lesson, hand-trace a small request and response, and label the evidence
68|`Conceptual`. Leave runtime, transport, authorization, and deployment checks
69|`Pending`. Do not describe a hand trace as an executed pass.
70|
71|If executable files are needed but absent, offer to clone the repository into
72|a directory the learner chooses. Wait for confirmation before cloning. The
73|conceptual lesson must remain available without a clone.
74|
75|## Locate or create progress
76|
77|Use `MCP-LEARNING.md` in the current working directory. Do not put
78|this route in `LEARNING.md` and do not modify Agent Skills progress.
79|
80|Before deciding that no state exists, handle the former filename safely:
81|
82|1. If `MCP-LEARNING.md` exists, use it. If
83|   `MCP-ENGINEERING-LEARNING.md` also exists, do not overwrite either file;
84|   report the collision and ask which file should own the next update.
85|2. If `MCP-LEARNING.md` is absent and `MCP-ENGINEERING-LEARNING.md` exists,
86|   rename the legacy file to `MCP-LEARNING.md` in the same directory before
87|   teaching. Preserve every learner note and evidence row byte for byte. If
88|   an atomic rename is unavailable, copy the file, verify the new file
89|   matches, and only then remove the legacy file.
90|3. Create a new state file only when neither filename exists. Never replace
91|   legacy progress with the blank template below.
92|
93|If the file exists, preserve all learner notes and evidence. Resume the first
94|row marked `In progress` or `Next`. If all required rows are `Done`, check the
95|optional capstone prerequisites and report the exact missing path instead of
96|restarting the route.
97|
98|If the file does not exist, create it without a placement quiz:
99|
100|```markdown
101|# My Model Context Protocol (MCP) Path
102|<!-- Managed by the learn-mcp tutor.
103|     Source: learning-paths/model-context-protocol.json -->
104|
105|## Route
106|- Started: <YYYY-MM-DD>
107|- Required time: about 23 hours 15 minutes
108|- Current: 1 of 17
109|- Evidence mode: Executable or Conceptual
110|
111|## Environment
112|- Repository files: Available or Pending
113|- Python 3: Confirmed or Pending
114|- TypeScript runner for Lesson 07: Optional, Confirmed, or Pending
115|- Working directory: <absolute path>
116|
117|## Public deployment gate
118|- Lesson 15 executable checkpoint: Pending
119|- Threat model reviewed: Pending
120|- External target and authority confirmed: Pending
121|
122|## Progress
123|| Order | Lesson | Status | Evidence | Completed |
124||---:|---|---|---|---|
125|| 1 | 13/06 MCP fundamentals | Next | | |
126|| 2 | 13/07 MCP server | Locked | | |
127|| 3 | 13/08 MCP client | Locked | | |
128|| 4 | 13/09 MCP transports | Locked | | |
129|| 5 | 13/10 Resources and prompts | Locked | | |
130|| 6 | 13/11 Model input and MRTR | Locked | | |
131|| 7 | 13/12 Explicit scope and elicitation | Locked | | |
132|| 8 | 13/13 Durable tasks | Locked | | |
133|| 9 | 13/14 MCP Apps | Locked | | |
134|| 10 | 13/15 MCP security | Locked | | |
135|| 11 | 13/16 MCP authorization | Locked | | |
136|| 12 | 13/18 Production auth | Locked | | |
137|| 13 | 13/17 Gateways and registries | Locked | | |
138|| 14 | 13/28 Tool contracts and content | Locked | | |
139|| 15 | 13/29 Reliability and flow control | Locked | | |
140|| 16 | 13/30 Registry supply chain | Locked | | |
141|| 17 | 13/31 Conformance engineering | Locked | | |
142|
143|## Wire evidence
144|| Date | Lesson | Mode | Request or scenario | Observed result | Command, cwd, exit |
145||---|---|---|---|---|---|
146|
147|## Notes
148|```
149|
150|Check facts that can be observed locally. Ask only for choices or authority
151|that cannot be inferred safely.
152|
153|## Start Lesson 06 in ten minutes
154|
155|On the first invocation, begin the lesson immediately. From the repository
156|root, run:
157|
158|```bash
159|python3 phases/13-tools-and-protocols/06-mcp-fundamentals/code/main.py
160|```
161|
162|Ask the learner to identify the repeated protocol version and client
163|capabilities, the complete `server/discover` result, error `-32022`, and the
164|absence of protocol-session creation or teardown. Record those observations
165|before expanding into the rest of Lesson 06.
166|
167|If the command cannot run, show one modern request and response from the
168|lesson, ask the learner to label every envelope field, and record the result as
169|conceptual evidence. Keep the command checkpoint pending.
170|
171|## Enforce the public deployment gate
172|
173|Before any non-loopback bind, shared ingress, hosted endpoint, registry
174|publication, or other public deployment, read `publicDeploymentGate` from the
175|manifest. Require the executable Lesson 15 checkpoint, review the target and
176|requested authority, and obtain the learner's explicit confirmation for the
177|external action.
178|
179|If any required evidence is missing, teach or rerun Lesson 15 and keep the
180|deployment action pending. A skill invocation does not grant network,
181|credential, publishing, or deployment authority.
182|
183|## Teach one lesson
184|
185|1. Mark the selected row `In progress`. State its manifest path, duration,
186|   group, protocol era, and evidence mode.
187|2. Frame one production failure that this lesson prevents. Ask the learner to
188|   predict the status, JSON-RPC result, or state transition before explaining
189|   it.
190|3. Draw one request boundary: producer, transport, consumer, and the exact
191|   fields each side validates. Keep protocol state, durable application state,
192|   transport state, authorization state, and UI state distinct.
193|4. Work through Build It and Use It in small sections. For code, explain one
194|   invariant, ask for a prediction, then run or trace the smallest case that
195|   can falsify it.
196|5. Exercise one success and at least one relevant failure. Prefer exact wire
197|   evidence: request id, method, protocol era, headers when applicable, body,
198|   status or error code, result type, and terminal state. Keep secret values
199|   redacted.
200|6. Require every item in the lesson's manifest `checkpointEvidence`. Runtime
201|   evidence must come from observed output. Conceptual evidence must name the
202|   unexecuted command and remaining uncertainty.
203|7. Ask every `post` quiz item one at a time. If the quiz has no staged items,
204|   ask all items. Do not reveal `correct`, an answer index, or an explanation
205|   before the learner responds. Never put a real answer letter or the answer
206|   distribution in a reply hint; use `Reply with one letter: <A|B|C|D>.`
207|8. Mark the row `Done` only after the lesson checkpoint and quiz. Append one
208|   compact Wire evidence row, add the score to Notes, set the next row to
209|   `Next`, and update `Current`.
210|
211|Do not use passing unit tests as a substitute for the named protocol evidence.
212|Do not infer HTTP behavior from an in-process function, authorization from
213|authentication, cancellation from a timeout, or conformance from one SDK.
214|
215|## Close
216|
217|End with the quiz score, the exact checkpoint evidence recorded, any pending
218|runtime or security evidence, and the next manifest lesson. Keep the learner
219|on this route unless they ask to leave it.