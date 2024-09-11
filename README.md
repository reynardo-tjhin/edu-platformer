# Educational Platformer Game

## Requirements

Please download all the required libraries/packages in the requirements.txt

```[python3]
pip install -r requirements.txt
```

## TODO List

- Integrate the platformer game to the mini-quiz
  - player leveled up and then can go to the next level
- Improve the designs of the pages
- Only for admin (or superuser) page
  - /mini-quiz/index: allow only for admins
  - /mini-quiz/index: can do CRUD (create, read, update & delete) on the mini-quiz
  - /mini-quiz/index: create new level
  - /mini-quiz/index: update the contents of each level
  - /mini-quiz/index: delete the level

## Bugs Tracking

- Currently player can only attempt the quiz ONCE
  - This is due to the way the data is saved.
  - An attempt is created and updated.
  - A new attempt on the same quiz is not created.
  - Hence, once the attempt is successfully completed, the attempt will permanently be saved as complete.
  - The next time the player attempts the quiz and failed, the message will still be successful.
- Player can directly access mini quiz questions withuot starting the mini quiz
