* Website: [phase.finance/](https://phase.finance/)
* Twitter: [@phaseyield](https://twitter.com/PhaseYield)
* Email: [contact@phase.finance](mailto:contact@phase.finance)* Slack: [uni-
* discord: [phaseyeild](https://discord.com/invite/YEk2Eyv)
* litepaper: [Link](https://www.docdroid.net/XXzk9U7/phase-litepaper-v1-pdf)

## Installation:

#### Requires [Python 3](https://www.python.org/download/releases/3.0/)

1) Uniswap Integration
```
$ git clone https://github.com/phasedex/contracts-vyper
$ cd contracts-vyper
```

2) Setup virtual environment
```
$ pip3 install virtualenv
$ virtualenv -p python3 env
$ source env/bin/activate
```

3) Install dependencies
```
pip install -r requirements.txt
```

4) (Optional) Switch Vyper compiler to version used in Uniswap [verification](https://github.com/runtimeverification/verified-smart-contracts/tree/uniswap/uniswap)  
```
cd vyper
git reset --hard 35038d20bd9946a35261c4c4fbcb27fe61e65f78
cd ..
```

5) Run tests
```
$ pytest -v tests/
```
