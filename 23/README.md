## HV19.23 Internet Data Archive

Today's flag is available in the Internet Data Archive (IDA).

### Resources

[http://whale.hacking-lab.com:23023/](http://whale.hacking-lab.com:23023/)

### Solution

```
manuel@ManuelErika:/mnt/d/Dokumente/hackvent-2019/23$ php crack.php | john --stdin santa.hash
Using default input encoding: UTF-8
Loaded 1 password hash (ZIP, WinZip [PBKDF2-SHA1 256/256 AVX2 8x])
Will run 8 OpenMP threads
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
Kwmq3Sqmc5sA     (Santa-data.zip/flag.txt)
1g 0:00:01:01  0.01619g/s 70300p/s 70300c/s 70300C/s suKcApykm6ST..Ekjreg8U85fm
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

**Flag:** HV19{Cr4ckin_Passw0rdz_like_IDA_Pr0}
