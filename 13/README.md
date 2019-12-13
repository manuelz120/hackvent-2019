## HV19.13 TrieMe

Switzerland's national security is at risk. As you try to infiltrate a secret spy facility to save the nation you stumble upon an interesting looking login portal.

Can you break it and retrieve the critical information?

### Resources

- Facility: http://whale.hacking-lab.com:8888/trieme/
- [HV19.13-NotesBean.java.zip](./34913db9-fd2a-43c8-b563-55a1d10ee4cb.zip)

### Solution

Trick the trie by appending a null-byte to the key: `auth_token_4835989\0`
Details follow.

![](./flag.jpg)

**Flag:** HV19{get_th3_chocolateZ}
