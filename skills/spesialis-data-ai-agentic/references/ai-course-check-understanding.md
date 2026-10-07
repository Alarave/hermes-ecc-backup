1|---
2|name: check-understanding
3|version: 1.0.0
4|description: Phase quiz for AI Engineering from Scratch. Trigger with "quiz me", "test phase", "check my understanding", "do I know phase 3", or `/check-understanding <phase>`.
5|---
6|
7|# Check Understanding
8|
9|Test your knowledge of a completed phase from the AI Engineering from Scratch course.
10|
11|## Activation
12|
13|This skill activates when the user says things like:
14|- `/check-understanding 3` or `/check-understanding deep-learning`
15|- "quiz me on phase 2"
16|- "test phase 1"
17|- "check my understanding of transformers"
18|- "do I know phase 3"
19|- "am I ready for the next phase"
20|
21|## Input
22|
23|Accepts a phase number (0-19) or a phase name as argument. If no argument is provided, ask the user which phase they want to be tested on by listing all 20 phases.
24|
25|## Phase Map
26|
27|Map the argument to the correct phase directory under `phases/`:
28|
29|| Input | Directory | Phase Name |
30||-------|-----------|------------|
31|| 0, setup, tooling | `00-setup-and-tooling` | Setup & Tooling |
32|| 1, math, math-foundations | `01-math-foundations` | Math Foundations |
33|| 2, ml, ml-fundamentals | `02-ml-fundamentals` | ML Fundamentals |
34|| 3, deep-learning, dl | `03-deep-learning-core` | Deep Learning Core |
35|| 4, cv, computer-vision, vision | `04-computer-vision` | Computer Vision |
36|| 5, nlp | `05-nlp-foundations-to-advanced` | NLP -- Foundations to Advanced |
37|| 6, speech, audio | `06-speech-and-audio` | Speech & Audio |
38|| 7, transformers | `07-transformers-deep-dive` | Transformers Deep Dive |
39|| 8, generative, gen-ai, genai | `08-generative-ai` | Generative AI |
40|| 9, rl, reinforcement-learning | `09-reinforcement-learning` | Reinforcement Learning |
41|| 10, llms, llm, llms-from-scratch | `10-llms-from-scratch` | LLMs from Scratch |
42|| 11, llm-engineering, llm-eng | `11-llm-engineering` | LLM Engineering |
43|| 12, multimodal | `12-multimodal-ai` | Multimodal AI |
44|| 13, tools, protocols, mcp | `13-tools-and-protocols` | Tools & Protocols |
45|| 14, agents, agent-engineering | `14-agent-engineering` | Agent Engineering |
46|| 15, autonomous | `15-autonomous-systems` | Autonomous Systems |
47|| 16, multi-agent, swarms | `16-multi-agent-and-swarms` | Multi-Agent & Swarms |
48|| 17, infrastructure, production, infra | `17-infrastructure-and-production` | Infrastructure & Production |
49|| 18, ethics, safety, alignment | `18-ethics-safety-alignment` | Ethics, Safety & Alignment |
50|| 19, capstone, projects | `19-capstone-projects` | Capstone Projects |
51|
52|## Procedure
53|
54|### Step 1: Resolve the Phase
55|
56|Parse the argument. If it is a number, validate it is between 0 and 19 inclusive. If the number is out of range, tell the user: "Phase [N] does not exist. Valid phases are 0-19." and show the full list for them to pick from. If it is a name or keyword, look it up in the Phase Map above. If the keyword does not match any entry in the map, tell the user: "Unknown phase '[keyword]'. Pick from the list below:" and present all 20 phases. If no argument is provided, ask the user to pick from the full list.
57|
58|### Step 2: Read the Phase Content
59|
60|If the repo is cloned (a `phases/` directory exists in or above the current directory), find all lesson directories under `phases/<phase-dir>/` and read each lesson's `docs/en.md`. If it is not cloned, get the phase's lesson list from the Contents section of the README (fetch `https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch/main/README.md`), then fetch each lesson's `docs/en.md` from the same raw base URL. These documents contain the teaching material you will generate questions from.
61|
62|Read as many lesson docs as needed to cover the full breadth of the phase. If a phase has many lessons (15+), prioritize reading a representative spread: first few, middle, and last few.
63|
64|### Step 3: Generate 8 Questions
65|
66|Create exactly 8 multiple-choice questions drawn from the lesson content you just read:
67|
68|**Questions 1-4: Conceptual (What/Why)**
69|These test understanding of ideas, definitions, and reasoning. Examples:
70|- "What is the purpose of X?"
71|- "Why does Y happen when Z?"
72|- "Which statement best describes the relationship between A and B?"
73|- "What problem does X solve?"
74|
75|**Questions 5-8: Practical (How/Build)**
76|These test applied knowledge and implementation awareness. Examples:
77|- "How would you implement X?"
78|- "Which approach correctly solves Y?"
79|- "What is the correct order of steps to build Z?"
80|- "If you observe X during training, what should you do?"
81|
82|Each question must have exactly 4 answer options labeled A, B, C, and D. Exactly one option is correct. The wrong options should be plausible but clearly incorrect to someone who studied the material.
83|
84|Tag each question with the specific lesson it draws from (e.g., "Lesson 03: Matrix Transformations").
85|
86|### Step 4: Present Questions One at a Time
87|
88|Use the AskUserQuestion tool (or equivalent interactive prompt) to present each question individually. Format:
89|
90|```text
91|Question 1/8 (Conceptual) -- from Lesson 03: Matrix Transformations
92|
93|What is the geometric interpretation of an eigenvalue?
94|
95|A) The angle of rotation applied by the matrix
96|B) The factor by which the eigenvector is scaled during transformation
97|C) The determinant of the transformation matrix
98|D) The rank of the matrix after transformation
99|```
100|
101|Wait for the user's answer before moving to the next question.
102|
103|### Answer isolation
104|
105|Keep the correct option and explanation private until the learner answers the
106|current question. Never use a real answer letter, a likely answer, or the
107|generated answer distribution in a reply-format hint. When a plain-text hint
108|is needed, use exactly: `Reply with one letter: <A|B|C|D>.`
109|
110|### Step 5: Track and Score
111|
112|Keep a running tally:
113|- Total correct out of 8
114|- For each wrong answer, record: the question number, the user's answer, the correct answer, and which lesson it came from
115|
116|### Step 6: Show Results
117|
118|After all 8 questions, display the score and grade:
119|
120|**7-8 correct: Mastered**
121|If the phase is 19 (Capstone Projects): "You have mastered Phase 19, the final phase." Add "Congratulations, you have completed the entire curriculum." only when you can verify the rest of the curriculum is done (a `LEARNING.md` in the current directory whose Path table shows Phases 0-18 as Done or Skip); a single phase quiz does not prove full completion.
122|Otherwise: "You have a strong grasp of Phase N. You are ready to move on to Phase N+1: [next phase name]."
123|
124|**5-6 correct: Almost**
125|"Solid foundation. Review these specific areas before moving on:"
126|Then list the lessons tied to the missed questions.
127|
128|**3-4 correct: Developing**
129|"You are building understanding but need to revisit some lessons:"
130|Then list each missed question with the lesson to re-read.
131|
132|**0-2 correct: Start Over**
133|"This phase needs more time. Work through the lessons again from the beginning, focusing on:"
134|Then list all missed topics.
135|
136|### Step 7: Wrong Answer Breakdown
137|
138|For every question the user got wrong, show:
139|
140|```text
141|Question N: [question text, abbreviated]
142|Your answer: B
143|Correct answer: C -- [the correct option text]
144|Why: [1-2 sentence explanation of why C is correct]
145|Review: Lesson NN -- [lesson name] (phases/<phase-dir>/NN-<lesson-slug>/docs/en.md)
146|```
147|
148|### Step 8: What Next?
149|
150|End by offering three choices:
151|
152|1. **Retake this quiz** -- generate a fresh set of 8 questions from the same phase
153|2. **Try another phase** -- pick a different phase to test
154|3. **Explain a topic** -- ask about any concept from the questions you missed
155|
156|Wait for the user's choice and act accordingly.
157|
158|## Rules
159|
160|- Avoid repeating questions on retakes until the question pool is exhausted. Once exhausted, reshuffle or rephrase questions for subsequent retakes.
161|- Questions must be directly grounded in the lesson docs, not general knowledge.
162|- Do not show the correct answer until after the user responds.
163|- Do not include literal answer letters in examples of how the learner should
164|  reply; use `<A|B|C|D>` as the placeholder.
165|- Keep question text concise. One or two sentences max.
166|- Wrong options must be plausible. No joke answers.
167|- If a phase has no lesson docs written yet (no `en.md` files found), tell the user: "Phase N does not have lesson content yet. Pick a completed phase to quiz on."