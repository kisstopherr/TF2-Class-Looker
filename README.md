# TF2-Class-Looker
A script to find enemy players classes in TF2.

## Setup

### Prerequisites

- At least Python 3.10 installed on your system.
- regular expressions installed.
- Team Fortress 2 installed.

### Installation

1. Clone the repository to your computer or download the files:

    ```sh
    git clone https://github.com/kisstopherr/TF2-Class-Looker.git
    cd TF2-Class-Looker
    ```
2. Install regular expressions or `re`:

   ```sh
   pip install re
   ```

### Setup

- Edit the `main.py` file, and to set the `tf2Path` variable as needed.

    ```python
    tf2Path = "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf"
    ```

## Usage

1. Run the bot:

    ```sh
    python main.py
    ```

2. The bot continuously monitors the `console.txt` file for relevant events:
    - When someone kills someone, the script gets the class from the `weapons.json` file.
    - When someone kills someone, the script also gets the players name. 

3. Keep the script running while playing Team Fortress 2.

# How it works

1. **Console Monitoring**:
    - The script reads `console.txt`, the game’s log file, every half second.
    - It extracts kills messages using regular expressions.

2. **Check for Player Weapons**:
    - When someone kills another player:
        - Their username is printed.
        - Their weapon is used to find their class in the `weapons.json`.

3. **Real-time Updates**:
    - The script uses `time.sleep(0.5)` to continuously scan for new events in the log.
