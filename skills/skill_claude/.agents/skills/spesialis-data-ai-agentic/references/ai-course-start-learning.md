1|---
2|name: start-learning
3|version: 1.0.0
4|description: >
5|  One-time onboarding for the AI Engineering from Scratch curriculum (523
6|  lessons, 20 phases). Interviews the learner, runs the placement quiz, and
7|  writes LEARNING.md, a persistent study plan the learn skill drives.
8|  Trigger phrases: "start learning", "set up the course", "begin the
9|  curriculum", "onboard me", "create my learning plan"
10|tags: [onboarding, curriculum, ai-engineering, learning-plan]
11|---
12|
13|# Start Learning
14|
15|You are onboarding a learner into the **AI Engineering from Scratch**
16|curriculum: 523 lessons across 20 phases, from linear algebra to autonomous
17|agents. Your job is to produce `LEARNING.md`, a single file in the current
18|directory that captures why they are learning, where they should start, and
19|what their path looks like. Every later `learn` session reads and updates
20|this file, so treat it as the learner's source of truth.
21|
22|Works with any agent. If your environment has a structured question/option
23|tool, use it for every question; otherwise present lettered options as plain
24|text and wait for the reply.
25|
26|## Host invocation contract
27|
28|Skill names are portable, but invocation syntax belongs to the host. Before
29|showing a next command, use the correct form:
30|
31|- Codex: `start-learning`, `learn`, `course-guide`, and other `skill-name`
32|  forms, or tell the learner to choose the skill from `/skills`.
33|- Claude Code: `/start-learning`, `/learn`, `/course-guide`, and other
34|  `/skill-name` forms.
35|- Other compatible hosts: natural language such as `Use learn to start my
36|  first lesson.`
37|
38|Never present a Claude Code slash command as universal syntax. When the host is
39|unknown, use the natural-language form.
40|
41|## Resume routing across course modes
42|
43|Before generic onboarding, resolve every "resume" or "continue" request
44|against these supported state files and their route owners:
45|
46|- `LEARNING.md` belongs to `learn` for the full curriculum.
47|- `MCP-LEARNING.md` belongs to `learn-mcp` for the Model Context Protocol
48|  (MCP) route.
49|- `MCP-ENGINEERING-LEARNING.md` is the legacy filename for that same
50|  `learn-mcp` route, not a separate route.
51|- `AGENT-SKILLS-LEARNING.md` belongs to `learn-agent-skills`.
52|- `CLAUDE-CERTIFICATION.md` belongs to `claude-certification`.
53|
54|If the learner names a route in a resume or continue request, dispatch to its
55|owner immediately even when other state files exist, then stop this skill.
56|
57|For an unnamed resume or continue request, collect the owners whose state files
58|exist, grouping both MCP filenames under `learn-mcp`. If exactly one route owner
59|remains, invoke it and stop this skill before generic onboarding. `learn-mcp`
60|owns legacy-file migration and collision reporting. If two or more route owners
61|remain, list their learner-facing route names and ask which route to resume
62|before running placement or changing any state. If none exist, continue with
63|generic onboarding. Never infer a route from file recency or merge one route's
64|progress into another state file.
65|
66|Legacy runtimes may expose `learn-mcp-engineering` as an alias. Accept it only
67|to reach `learn-mcp`; render every learner-facing handoff as `learn-mcp` and
68|name the route Model Context Protocol (MCP).
69|
70|## Focused MCP handoff
71|
72|If the learner explicitly wants Model Context Protocol (MCP) rather than the
73|full course, do not run placement and do not create `LEARNING.md`. Route to
74|the portable skill `learn-mcp`, whose source is
75|`learning-paths/model-context-protocol.json` and whose state file is
76|`MCP-LEARNING.md`. Use `learn-mcp` in Codex,
77|`/learn-mcp` in Claude Code, or ask another compatible host to use
78|`learn-mcp`. The dedicated tutor owns lesson selection, wire
79|evidence, and the public-deployment security gate.
80|
81|## Focused Agent Skills handoff
82|
83|If the learner explicitly wants Agent Skills instead of the full course, or
84|`AGENT-SKILLS-LEARNING.md` exists and they ask to resume that route, do not run
85|placement and do not create `LEARNING.md`. Route to the portable skill
86|`learn-agent-skills`, whose source is `learning-paths/agent-skills.json` and
87|whose state file is `AGENT-SKILLS-LEARNING.md`. Use `learn-agent-skills` in
88|Codex, `/learn-agent-skills` in Claude Code, or ask another compatible host to
89|use `learn-agent-skills`. The dedicated tutor owns the five-lesson order,
90|real-host evidence, sandbox boundaries, the Lesson 25 and tool-poisoning
91|prerequisite gate before Lesson 26, and the release gate.
92|
93|If `LEARNING.md` already exists, do not overwrite it. Summarize what it says
94|(mission, entry point, progress so far) and offer exactly three paths:
95|
96|- **Resume**: invoke `learn` with the host syntax above; skip the interview and
97|  placement entirely.
98|- **Re-run placement**: administer the quiz again, then update only the
99|  Placement section and the Path statuses; keep the Mission, the Progress
100|  log, and the Review queue untouched.
101|- **Start over**: only after an explicit confirmation, rename the current
102|  file to `LEARNING-<YYYY-MM-DD>.md` as an archive, then proceed with the
103|  full onboarding below. Never delete or overwrite their history silently.
104|
105|## Step 1: The interview (3 questions, keep it short)
106|
107|1. **Why are you learning AI engineering?** Free text. Examples to offer:
108|   ship an AI product, career change, understand what I already use daily,
109|   research. Capture their answer in their own words because it grounds every
110|   future lesson explanation.
111|2. **How much time per week?** Options: ~2 h, ~5 h, ~10 h, "as fast as
112|   possible". Used only to phrase the pace honestly, never to cut content.
113|3. **What do you most want to build by the end?** One line. An agent, a
114|   trained model, a RAG product, "not sure yet" is fine.
115|
116|Do not ask more than these three. The placement quiz measures knowledge;
117|the interview only captures intent.
118|
119|## Step 2: Placement
120|
121|Run the placement quiz from the `find-your-level` skill (it installs
122|alongside this one): 5 areas, 10 questions, mapped to an entry phase. Preserve
123|that skill's answer-isolation contract: do not preload later answer-key rounds
124|or replace neutral `<letter>` placeholders with real option letters.
125|
126|If the learner says they already know where they want to start ("just start
127|me at phase 7"), respect that and skip the quiz, with the same output
128|contract as a quiz run so the `learn` tutor always finds a well-formed plan:
129|
130|- Validate the phase is 0-19 and resolve its canonical name; if it does not
131|  resolve, list the 20 phases and ask them to pick.
132|- In the Path table: phases below the entry point are `Skip`, the entry
133|  point and everything above are `Do` (no `Review` rows because there are no area
134|  scores to infer them from), and the Est. hours total is the sum of the
135|  `Do` rows.
136|- In the Placement section write `Score: self-selected` instead of a
137|  number.
138|
139|## Step 3: Write LEARNING.md
140|
141|Create `LEARNING.md` in the current directory with exactly these sections:
142|
143|```markdown
144|# My AI Engineering Path
145|<!-- Managed by the ai-engineering-from-scratch learning skills.
146|     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->
147|
148|## Mission
149|<their answer to question 1, in their words, plus the build goal from question 3>
150|
151|## Placement
152|- Date: <YYYY-MM-DD>
153|- Score: <total>/10 with the area breakdown, or exactly `self-selected` when the quiz was skipped
154|- Entry point: Phase <N>: <name>
155|- Pace: ~<hours>/week
156|
157|## Path
158|| Phase | Name | Status | Est. hours |
159||-------|------|--------|------------|
160|<all 20 phases; Status is Skip, Review, Do, or Done from the placement
161|result. Hours come from ROADMAP.md: read it locally if the repo is cloned,
162|otherwise fetch
163|https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch/main/ROADMAP.md>
164|
165|## Progress log
166|| Date | Lesson | Quiz | Note |
167||------|--------|------|------|
168|
169|## Review queue
170|<empty for now; learn adds lessons the quizzes flag>
171|```
172|
173|## Step 4: Hand off
174|
175|Close with three lines, nothing more:
176|
177|- Their entry point and total estimated hours for the Review + Do phases.
178|- Give the host-correct invocation for `learn` and say that it starts the first
179|  lesson and picks up from this file every time.
180|- Give the host-correct invocation for `course-guide <topic>` and say that it
181|  can jump to a specific topic instead.