# asyncping

异步调用系统ping工具，返回该ip是否丢包、

```
from asyncping import ping, simping

print(simping('127.0.0.1')) # True

# 并发ping参考main.py
```

## TODO
* ~~支持同步和异步调用~~