# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 

The game was set on difficulty normal the first time with 7 attempts allowed to guess a number between 1 and 100. There was a developer debug info menu that showed secret, attempts, score, difficulty, and history. There was an option to enter a guess number, submit guess, new game, and a checkmarked show hint box. There was a history that was logging each guess attempt and the hint was telling me to guess lower with each guess.


- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").  
  1. The first concrete bug I noticed was that on the Normal difficulty setting level, there were 7 attempts allowed to guess a number between 1 and 100 while the Easy difficulty level allowed 5 attempts to guess a number a number between 1 and 100. Lowering the difficulty resulted in less opportunity (guess attempts) to guess the number with the same range of 1 to 100, which actually makes the game harder as the difficulty level is set to an easier diffuclty level. There should be more guess attempts allowed when the difficlty level is changed from normal to easy. 
  2. The second concrete bug I noticed was that the Normal difficulty level required guessing a number from 1 to 100 while the Hard difficulty level required guessing a number from 1 to 50. When the range of numbers to guess is smaller and there is less chance of guessing the wrong number, the game actually becomes easier on the Hard difficulty level. Therefore, there should be a range greater than 1 to 100 to guess on the hard difficulty level rather than the existing 1 to 50 range of numbers to guess. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
