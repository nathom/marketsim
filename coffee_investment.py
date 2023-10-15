from dataclasses import dataclass


@dataclass
class IdealInvestment:
    rate_of_return: float
    compounds_per_year: int
    balance: float = 0
    day: int = 1

    def add_balance(self, amt):
        self.balance += amt

    def next_day(self):
        compounded_every = 365 // self.compounds_per_year
        if self.day % compounded_every == 0:
            self.balance += self.balance * (
                self.rate_of_return / self.compounds_per_year
            )
        self.day += 1


@dataclass
class ActualInvestment:
    data: list[float]
    timescale: int
    day: int
    num_shares: float = 0

    def buy(self, dollars):
        current_price = self.data[self.day]
        self.num_shares += dollars / current_price

    def next_day(self):
        self.day += 1

    def value(self) -> float:
        return self.num_shares * self.data[self.day]


def main():
    timeframe = 11 * 30
    snp500 = IdealInvestment(0.0488, 12)
    print(snp500)
    snp500.add_balance(5000)
    for _ in range(timeframe):
        snp500.next_day()
    print(snp500.balance)

    # cd = IdealInvestment(0.0588, 12, 10000)
    # for _ in range(11 * 30):
    #     cd.next_day()
    # print(cd)


if __name__ == "__main__":
    main()
