# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  The website appears "deployable" at first glance: the instructions make sense, and everything you would expcet to be there is present, such as the input field, the submit button, the new game button, and the difficulty button. However, pressing enter on the first guess doesn't do anything. No hint appeared, my attempts didn't decrease, and my guess was not registered in the array. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  1) The hint kept telling me to guess lower even though the secret showed that my number was higher.

  2) The attemps don't correctly decrease as the difficulty increase. Easy mode has 6 attempts while medium has 8 and hard has 5.

  3) The instructions in the blue info box don't align with the instructions under the selected difficulty in the left column. The column shows that easy difficulty should select a number from 1-10, medium from 1-100 and hard from 1-50, but the blue box states that it's a number from 1-100 for all three.

  4) Building off of the last point, it doesn't make sense for medium difficulty to pick a number from 1-100 while hard selects a number from 1-50. The code makes it unclear if an increase in difficulty correlates with an increase in the range of numbers or a decrease in the number of attemps, or both.
  
  5) The attempts refresh when a different difficulty is selected, but the red game over banner still shows up, telling us to start a new game. Switching to a different ddifficulty should automatically start a new game and remove the red banner.
  
  6) Pressing new game selects a new number but does not clear the array, remove the red game over banner, or allow the user to submit new guesses.
  
  7) The secret number changes every time an attempt is submitted, rather than staying static until the user presses new game.

  8) When you run out of attempts, the red banner warns you that you ran out, but the blue info box still shows that you have 1 attempt remaining. 

  9) The input field allows you to submit number (negative and positive) outside the requested range, as well as characters and strings.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  
  I used the Claude extension.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  To solve the issue of the secret number changing with each guess, the AI suggested to remove the if-else statement in lines 159-163 of app.py. The AI clarified that the secret number was not actually changing, but that the number being displayed was changing due to the secret number being coverted into a string on the even-numbered attempts in the if-statement.

  I deleted the code as it stated, ater verifying myself that the code was not necessary for the method to work, and played a few rounds to ensure the secret number did not change. The bug was resolved.  

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  I asked the AI how to fix the error that resulted in the submit button having to be pressed twice for the attempts at the top to properly update. The AI suggested moving the st.info() line below if-submit block. I followed its instructions and verified via running the app. However, this resulted in the blue info bar being moved to the bottom of the screen, and it doesn't make sense for it to logically be there. I wanted to fix the issue *without* moving the location of the info.


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  
  I asked the AI to run a pytest with the expected output, and I visually confirmed it myself by running the app and verifying the fix worked. 

- Describe at least one test you ran (manual or using pytest)  
and what it showed you about your code.

  When trying to fix the issue described above (having to press submit twice for the attempts count to update), I realized that moving the location of the code not only affected the logic but also the UI (as moving my code also moved the info bar's location on the screen). This made me realize I had to be extra careful about the changes I made in the code as they would also affect the layout.

- Did AI help you design or understand any tests? How?

  Yes, it did help me understand. It provided me with more robust tests (for examples, recommendation for other test cases I could try) so that I could verify the code ran under all possible scenarios.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  It was a render issue. Since the number was being cast to a string on even attempts, the secrent number was visually changing to the numerical equivalent of the string's value.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  I would explain that Streamlit runs top to bottom, so the code is executed sequentially. I would explain that the order of the code is extra important as rendering variables before updating their value will cause the changes to not be displayed, since the old value is shown before it is changed. 

- What change did you make that finally gave the game a stable secret number?

  I removed the if statement that casted the secret number to a string, as the line of code served no purpose aside from introducing a bug.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? This could be a testing    habit, a prompting strategy, or a way you used Git.

  Runnign tests not just manually but also by using pytest. Being able to verify that my code works as intended into two seperate ways decreases the chances for bugs/errors.

- What is one thing you would do differently next time you work with AI on a coding task?

  Use the inline chat feature more. I usually type it into the general chat but it takes much longer since Claude automatically searches through multiple files, sometimes even when unnecessary. Using inline chat returned on average faster results. 

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  AI-generated code is very convenient. It saves a lot of time, at the cost of precious limited resources and environmental pollution...so I still feel deep guilt using it to carry out taks I can realistically do myself, even if it takes longer. In addition, I can trust the AI-code only because I understand every line's purpose. So working with AI just reminds me how important it is that I keep refreshing on my own knowledge. 
