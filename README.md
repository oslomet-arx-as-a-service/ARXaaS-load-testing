# ARXaaS load testing

Contains scripts and notebooks for load testing and analyzing load handling of ARXaaS


### Locust tests

Example run
```bash
python -m locust.main -f scripts/analyze_locust_test.py --host http://localhost:8080
```
Without Web UI and with time limit and saving to csv

```
python -m locust.main -f scripts/analyze_locust_test.py --host http://localhost:8080 --no-web -c 2 -r 1 --run-time 1m --csv=example -t30s
```

```
python -m locust.main -f scripts/analyze_locust_test.py --host http://localhost:8080 --no-web -c 1 -r 1 --run-time 1m --csv=analyze_1_5mill-rows
```
