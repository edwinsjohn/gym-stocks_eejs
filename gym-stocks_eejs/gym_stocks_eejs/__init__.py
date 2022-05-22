from gym.envs.registration import register
register(
    id="stocks_eejs",
    entry_point="gym_stocks_eejs.envs:Stocks_eejs",
)