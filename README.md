
# Household-Account
Save Money in Times of High Inflation

<img src="https://blog.kakaocdn.net/dn/tPPrk/btsJPCAM1gP/3kNpktpRlAmnfKt4E6bhOK/img.png" width=410 />

# USE
```bash

$ Household-Account <Expense> <Category>

$ household-account --help

 Usage: household-account [OPTIONS] EXPENSES CATEGORY

╭─ Arguments ────────────────────────────────────────────────────╮
│ *    expenses      INTEGER  [default: None] [required]         │
│ *    category      TEXT     [default: None] [required]         │
╰────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                    │
╰────────────────────────────────────────────────────────────────╯

$ household-account 10000 식비
식비에 10000를 썼습니다. 이는 효율적인 소비입니다.
총 지출 : 10000원

$ household-account 60000 교통비
그럴만할 일이 있었겠지..딱한것..
총 지출 : 60000원

```

## DEV
```bash
$ git clone ...
$ pdm venv create
$ source .venv/bin/activate
$ pdm install
$ pytest
```
