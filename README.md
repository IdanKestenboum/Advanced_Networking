## Commands to show stats and tcpdump

```
watch -n 1 "echo -n 'CPU: '; top -b -n1 | grep 'Cpu(s)' | awk '{print \$2 + \$4 \"% usage\"}'; \
echo -n '  MEM: '; free | grep Mem | awk '{printf(\"%.1f%% used\", (\$3/\$2)*100)}'; \
echo -n '  SYN_RECV: '; netstat -an | grep :9090 | grep SYN_RECV | wc -l; \
echo -n '  TCP_ESTABLISHED: '; netstat -an | grep :9090 | grep ESTABLISHED | wc -l"
```


'''
tcpdump -i eth0 -n -l 'tcp port 9090 and (tcp[13] & 2 != 0)' 2>/dev/null \
| awk '/Flags \[S/ {
    src = $3;
    dst = $5;
    gsub(/\./, ":", src);
    gsub(/\./, ":", dst);
    sub(/:$/, "", dst);
    print "source: {" src "} -> dest: {" dst "} " $6, $7
}'
```
