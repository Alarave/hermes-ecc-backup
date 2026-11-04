1|---
2|name: find-your-level
3|version: 1.0.0
4|description: >
5|  Interactive quiz that maps your AI/ML knowledge to a starting point in the
6|  523-lesson, 20-phase AI Engineering from Scratch curriculum.
7|  Trigger phrases: "where should I start", "find my level", "what do I know",
8|  "which phase", "assess my knowledge", "placement test", "skip ahead"
9|tags: [assessment, onboarding, curriculum, ai-engineering]
10|---
11|
12|# Find Your Level
13|
14|You are administering a placement quiz for the **AI Engineering from Scratch**
15|curriculum (20 phases, 523 lessons). Your job is to figure out where the
16|learner should begin so they skip material they already know and land right
17|where the challenge starts. Works with any agent.
18|
19|## Quiz Structure
20|
21|There are 5 knowledge areas, 2 questions each, 10 questions total. Present
22|them in rounds of 2 (one round per area). After the learner answers both
23|questions in a round, score that area before moving on.
24|
25|## Scoring
26|
27|Each question is worth 1 point (0 = wrong or blank, 1 = correct). Each area
28|scores 0-2. Total score ranges from 0 to 10.
29|
30|## Administering the Quiz
31|
32|Start by greeting the learner briefly, then jump straight into Round 1. If
33|your environment has a structured question/option tool, use it for every
34|question; otherwise present the lettered options as plain text and wait for
35|the reply. After each round, tell the learner their score for that area
36|(e.g. "Math & Statistics: 2/2") before moving to the next round. Keep
37|commentary short. Do not explain the answers until the very end.
38|
39|### Answer isolation
40|
41|The answer key is intentionally stored in `references/answer-key.md`, outside
42|this quiz body. Do not read that reference before the learner submits both
43|answers for the current round. Then read only that round's key, score it, and
44|keep its explanation private until all five rounds are complete. Do not preload
45|later rounds.
46|
47|Never put a real answer letter, a likely answer, or the answer distribution in
48|a reply-format example. For plain text, use this neutral prompt exactly:
49|`Reply with Q1: <letter>, Q2: <letter>.` Substitute the current question
50|numbers, but keep both values as `<letter>`.
51|
52|---
53|
54|### Round 1 -- Math & Statistics
55|
56|**Q1.** You have two vectors, a = [1, 2, 3] and b = [4, 5, 6]. What is their
57|dot product?
58|
59|- A) 32
60|- B) 21
61|- C) 15
62|- D) 27
63|
64|**Q2.** A fair coin is flipped 3 times. What is the probability of getting
65|exactly 2 heads?
66|
67|- A) 1/4
68|- B) 1/2
69|- C) 1/8
70|- D) 3/8
71|
72|---
73|
74|### Round 2 -- Classical ML
75|
76|**Q3.** In a classification task with 90% negative and 10% positive samples,
77|a model predicts everything as negative. What is its accuracy?
78|
79|- A) 50%
80|- B) 90%
81|- C) 10%
82|- D) 0%
83|
84|**Q4.** Which of the following is a hyperparameter of a Random Forest?
85|
86|- A) The learned split thresholds
87|- B) The leaf node predictions
88|- C) The number of trees
89|- D) The Gini impurity at each node
90|
91|---
92|
93|### Round 3 -- Deep Learning
94|
95|**Q5.** During backpropagation, what does the chain rule compute?
96|
97|- A) The loss gradient for each trainable weight
98|- B) The best learning rate for the current optimizer
99|- C) The exact number of layers the network requires
100|- D) The batch size used for each training step
101|
102|**Q6.** What problem do residual connections (skip connections) in ResNet
103|primarily address?
104|
105|- A) Poor generalization on small training datasets
106|- B) Slow loading of batches from persistent storage
107|- C) High activation memory during model inference
108|- D) Weak gradient flow through very deep networks
109|
110|---
111|
112|### Round 4 -- NLP & Transformers
113|
114|**Q7.** In the Transformer architecture, what does the attention mechanism
115|compute between?
116|
117|- A) Pixels and labels
118|- B) Encoder and Decoder only
119|- C) Queries, Keys, and Values
120|- D) Embeddings and positions only
121|
122|**Q8.** What is the main benefit of LoRA (Low-Rank Adaptation) when
123|fine-tuning a large language model?
124|
125|- A) It retrains every base-model parameter from a completely fresh initialization
126|- B) It trains low-rank adapters while the base-model weights stay frozen
127|- C) It removes the need for labeled examples or task-specific training data
128|- D) It duplicates the model layers to increase its adaptation capacity
129|
130|---
131|
132|### Round 5 -- Applied AI
133|
134|**Q9.** In a RAG (Retrieval-Augmented Generation) system, what happens before
135|the LLM generates an answer?
136|
137|- A) Relevant documents are retrieved and added to the model prompt
138|- B) The whole model is fully retrained on the user's current question
139|- C) The user selects every context passage before each model request
140|- D) The model searches only its pretrained parameter values
141|
142|**Q10.** In a multi-agent system, what is the primary purpose of a
143|"coordinator" or "orchestrator" agent?
144|
145|- A) To replace every specialist agent with one general-purpose model
146|- B) To assign tasks, route messages, and coordinate the other agents
147|- C) To maximize token usage across every agent interaction
148|- D) To keep an identical backup model ready for system failures
149|
150|---
151|
152|## After All 5 Rounds
153|
154|Display the area breakdown and total:
155|
156|```text
157|Math & Statistics:    X/2
158|Classical ML:         X/2
159|Deep Learning:        X/2
160|NLP & Transformers:   X/2
161|Applied AI:           X/2
162|----------------------------
163|Total:                X/10
164|```
165|
166|## Score-to-Entry-Point Mapping
167|
168|| Total Score | Entry Point | What It Means |
169||-------------|-------------|---------------|
170|| 0-3 | Phase 1: Math Foundations | Start from the ground up |
171|| 4-5 | Phase 3: Deep Learning Core | You have math and ML basics |
172|| 6-7 | Phase 7: Transformers Deep Dive | You know DL, time for transformers |
173|| 8-9 | Phase 11: LLM Engineering | Strong foundations, go straight to LLM apps |
174|| 10 | Phase 14: Agent Engineering | You know it all, build agents |
175|
176|## Personalized Learning Path
177|
178|After revealing the entry point, generate a markdown table covering all 20
179|phases. Use the score to determine the status of each phase. Phases below the
180|entry point get "Skip" (the learner already knows the material). Phases at or
181|above the entry point get "Do". If a learner scored 1/2 in an area that maps
182|to a skippable phase, mark that phase as "Review" instead of "Skip".
183|
184|Area-to-phase mapping for review detection:
185|- Math & Statistics (1/2) -> mark Phase 1 as "Review"
186|- Classical ML (1/2) -> mark Phase 2 as "Review"
187|- Deep Learning (1/2) -> mark Phase 3 as "Review"
188|- NLP & Transformers (1/2) -> mark Phases 5 and 7 as "Review"
189|- Applied AI (1/2) -> mark Phase 14 as "Review"
190|
191|Read the time estimates from ROADMAP.md (the canonical source of truth). Each
192|phase heading contains the estimated hours in the format `(~N hours)`. Parse
193|these values instead of using hardcoded numbers. This ensures the learning path
194|stays in sync with the roadmap as estimates are updated. If the repo is not
195|cloned locally, fetch it from
196|`https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch/main/ROADMAP.md`.
197|
198|## Output Format
199|
200|Generate the table like this:
201|
202|```markdown
203|| Phase | Name | Status | Est. Hours |
204||-------|------|--------|------------|
205|| 0 | Setup & Tooling | Skip | -- |
206|| 1 | Math Foundations | Review | 30 |
207|| 2 | ML Fundamentals | Skip | -- |
208|| 3 | Deep Learning Core | Do | 20 |
209|| ... | ... | ... | ... |
210|```
211|
212|Rules for the table:
213|- "Skip" phases show `--` for hours (they do not count toward the total)
214|- "Review" phases show full hours (the learner should skim them)
215|- "Do" phases show full hours
216|- Phase 0 (Setup & Tooling) is always "Skip" regardless of score (it is
217|  tooling setup, not knowledge)
218|- Sum the hours for "Review" and "Do" phases and show the total at the bottom
219|
220|After the table, add one sentence with the estimated total: "Your personalized
221|path: ~X hours across Y phases."
222|
223|Then add a brief recommendation: which phase to start with, and what to focus
224|on first based on their weakest area.
225|
226|Finally, offer the next step: `/start-learning` saves this placement into a
227|persistent `LEARNING.md` study plan, and `/learn` starts the first lesson,
228|taught interactively.