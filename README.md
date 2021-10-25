# weblog_helper

This tools helps to analyze a standard HTTP access logs.

## Feature 1:
Return all log lines that correspond to a given source IP address.

```weblog_helper.py 178.93.28.59```

## Feature 2:
Return all log lines that correspond to a given source CIDR range.

```weblog_helper.py 178.93.28.59/32``` OR ```weblog_helper.py 157.55.39.180/30```