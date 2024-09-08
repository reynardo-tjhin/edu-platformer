# Educational Platformer Game

## Requirements

Please download all the required libraries/packages in the requirements.txt

```[python3]
pip install -r requirements.txt
```

## Bugs Tracking

- Currently player can only attempt the quiz ONCE
  - This is due to the way the data is saved.
  - An attempt is created and updated.
  - A new attempt on the same quiz is not created.
  - Hence, once the attempt is successfully completed, the attempt will permanently be saved as complete.
  - The next time the player attempts the quiz and failed, the message will still be successful.
