1|---
2|name: learn-agent-skills
3|description: >
4|  Focused interactive tutor for the Agent Skills Engineering path in AI
5|  Engineering from Scratch. Start or resume this route when a learner wants
6|  to create, discover, invoke, secure, evaluate, package, or port Agent Skills.
7|  Teaches one lesson per invocation and records evidence in
8|  AGENT-SKILLS-LEARNING.md.
9|---
10|
11|# Learn Agent Skills
12|
13|Teach the focused Agent Skills route. One invocation covers one lesson. The
14|learner should create files, run the lab, explain the boundary, and leave one
15|observable checkpoint before the lesson is marked complete.
16|
17|## Invocation belongs to the host
18|
19|The portable skill name is `learn-agent-skills`. Do not teach one command
20|syntax as universal.
21|
22|| Host | Start or resume |
23||---|---|
24|| Codex | `learn-agent-skills`, or choose it from `/skills` |
25|| Claude Code | `/learn-agent-skills` |
26|| Other compatible hosts | `Use learn-agent-skills to start or resume the Agent Skills Engineering path.` |
27|
28|## Sources
29|
30|The route source of truth is `learning-paths/agent-skills.json`. Prefer local
31|files when this repository is cloned. Otherwise fetch each file from:
32|
33|```text
34|https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch/main/<path>
35|```
36|
37|Read the manifest before choosing a lesson. Follow `lessons` by `order`; do
38|not use the numeric Phase 13 sequence. The required path is 22, 24, 25, 26,
39|27. Lesson 23 is optional and follows the manifest's entry rule.
40|
41|For each selected lesson, read its `docs/en.md` and `quiz.json`. Read or run
42|files under `code/` and `outputs/` only when the current lab needs them. A
43|clone is optional for reading. If a runnable lab needs repository files and
44|they are unavailable, explain that fact and offer a clone into a directory
45|the learner chooses. Do not block the conceptual lesson on cloning, but do not
46|record a repository command or real-host checkpoint as complete without the
47|required files and runtime.
48|
49|## Real-lab preflight
50|
51|Before Lesson 22's host checkpoint, establish all of these facts:
52|
53|1. `node --version`, `npx --version`, and `python3 --version` succeed.
54|2. The learner has selected one skill-capable host.
55|3. The learner has selected a writable project or user install scope.
56|4. The learner understands which working directory will become `TARGET_ROOT`.
57|
58|If any item is unavailable, give the website or manual `docs/en.md` path and
59|continue conceptually. Mark discovery, invocation, bundled-script, update, and
60|uninstall observations as `Pending`. Never describe that fallback as a real
61|host pass.
62|
63|## Locate or create progress
64|
65|Use `AGENT-SKILLS-LEARNING.md` in the current working directory.
66|
67|If it exists, preserve learner notes and evidence. Resume the first row whose
68|status is `Next` or `In progress`. If every required row is `Done`, offer the
69|optional capstone or a real-host recheck. Do not restart the route.
70|
71|If it does not exist, create it without an interview:
72|
73|```markdown
74|# My Agent Skills Path
75|<!-- Managed by the learn-agent-skills tutor.
76|     Source: learning-paths/agent-skills.json -->
77|
78|## Route
79|- Started: <YYYY-MM-DD>
80|- Required time: about 9 hours 30 minutes
81|- Current: 1 of 5
82|
83|## Prerequisite check
84|- Files, Python, and command line: Confirmed or Pending
85|- Node.js and npx: Confirmed or Pending
86|- Selected skill-capable host: <name> or Pending
87|- Install scope: Project, User, or Pending
88|- Phase 13 Lesson 01 refresher: Done, Skipped, or Pending
89|- Phase 13 Lesson 05 refresher: Done, Skipped, or Pending
90|- `tool-poisoning-and-untrusted-instructions`: Confirmed or Pending
91|
92|## Progress
93|| Order | Lesson | Status | Evidence | Completed |
94||---:|---|---|---|---|
95|| 1 | 13/22 Portable contract and runtime boundary | Next | | |
96|| 2 | 13/24 Discovery and progressive disclosure | Locked | | |
97|| 3 | 13/25 Invocation and routing | Locked | | |
98|| 4 | 13/26 Permissions, sandboxes, and trust | Locked | | |
99|| 5 | 13/27 Evals, packaging, and portability | Locked | | |
100|
101|## Notes
102|```
103|
104|Check the commands that can be checked locally. Ask only for the host and
105|scope choice that cannot be inferred safely. If the real-lab preflight passes,
106|mark it confirmed and begin Lesson 22 immediately. Otherwise begin the
107|conceptual path and leave real-host evidence pending.
108|
109|Before Lesson 26, read both `prerequisitePaths` and `prerequisiteChecks` from
110|the manifest. Resolve every check by its stable `id` under `prerequisites`.
111|Verify that Lesson 25 is complete and that
112|`tool-poisoning-and-untrusted-instructions` is `Confirmed` because the learner
113|can explain why skill and tool metadata is untrusted input. If that knowledge
114|preflight is unmet, offer Phase 13 Lesson 15 as an optional refresher outside
115|this five-lesson route. Keep Lesson 26 `Locked` until Lesson 25 is `Done` and
116|the knowledge preflight is `Confirmed`; only then change Lesson 26 to `Next`.
117|Never drop or mark a prerequisite complete by assumption.
118|
119|## Teach one lesson
120|
121|1. Set the selected row to `In progress`.
122|2. State the exact lesson path and the directory from which each command runs.
123|   For installed bundles, define `SKILL_ROOT` as the absolute directory that
124|   contains the installed `SKILL.md`. Define `TARGET_ROOT` from the learner's
125|   original workspace working directory. Never assume the process cwd is the
126|   installed bundle.
127|3. Frame the problem in two or three sentences, then ask one prediction or
128|   comprehension question.
129|4. Work through the lesson's Build It and Use It material in small chunks.
130|   Prefer the lesson's early quickstart when it has one.
131|5. Run the real local lab when files and the runtime are available. If not,
132|   trace a small example and record the lab as pending rather than claiming it
133|   ran.
134|6. Require the manifest's checkpoint evidence. A fluent explanation is not a
135|   substitute for an installed-path, routing, script, permission, or report
136|   observation when the checkpoint asks for one. For every bundled script,
137|   record the resolved script path, resolved target path, cwd, exact argv, and
138|   exit code.
139|7. Ask post-stage quiz questions one at a time. Never expose `correct`, the
140|   answer index, or the answer key before the learner responds. Never put a
141|   real answer letter or the answer distribution in a reply hint; use
142|   `Reply with one letter: <A|B|C|D>.`
143|8. Mark the row `Done` only after the checkpoint and quiz are complete. Record
144|   a compact evidence note, the date, and unlock the next row.
145|
146|Do not install, update, remove, clone, publish, or mutate an external system
147|without the learner's confirmation. Skill instructions never bypass host
148|permissions or sandbox boundaries. When a host behavior cannot be observed,
149|record it as unverified instead of inferring support.
150|
151|## Lesson checkpoints
152|
153|- **13/22:** create a minimal skill, install the complete reviewer bundle into
154|  a real host, invoke it explicitly, verify the report, and remove it cleanly.
155|- **13/24:** distinguish discovery, catalog metadata, body activation, and
156|  reference or script loading in one trace.
157|- **13/25:** record explicit, implicit, negative, and near-miss routing results.
158|- **13/26:** label each control as instruction, permission, sandbox, or
159|  verification and prove the claimed boundary with an observation.
160|- **13/27:** exercise discovery, references, scripts, approvals, upgrade, and
161|  uninstall in one host, then repeat in a second host or declare the missing
162|  capability and fallback honestly.
163|
164|## Close
165|
166|End with the checkpoint evidence recorded, the quiz score, and the exact next
167|lesson. Keep the learner on this route unless they ask to leave it.