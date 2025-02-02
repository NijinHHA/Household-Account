import typer
import pandas as pd

def hha():
    return pd.DataFrame(data)

data = {"날짜" : [1,2,3,4,5,6,7,8,9,10],
        "지출" : [10000, 15000, 55000, 20000, 2000, 100000, 40000, 0, 10000, 20000],
        "수입" : [0, 0, 0, 0, 0, 0, 0, 800000, 0, 0],
        "카테고리" : ["식비", "식비", "교통비", "의료비", "택시비", "경조사비", "의류비", "생활비", "식비", "택시비"]}

df = pd.DataFrame(data)

#분석
def analyze_budget(df):
    total_expenses = df["지출"].sum()
    total_income = df["수입"].sum()
    balance = total_income - total_expenses
    return f"===가계부===\n총 지출: {total_expenses:,} 원\n총 수입: {total_income:,} 원\n총 합계 금액(잔액): {balance:,} 원\n==================="

# 메인작업함수
def process_budget():
    df = hha()

    r = analyze_budget(df)
    print(r)

def entry_point():
    typer.run(process_budget)







