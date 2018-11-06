class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        if 12 < len(s) or len(s) < 4: 
            return []

        r = []
        def bt(i=0, ip=['']):
            #print(i, ip)            
            if i == len(s) and len(ip) == 4:
                r.append('.'.join(ip))
                return
            if (len(ip) >= 4 and len(ip[-1]) == 3) or i == len(s): return
            

            if len(ip[-1]) == 0:
                ip[-1], i = s[i], i+1
                if ip[-1] == '0':
                    if len(ip) < 4:
                        ip.append('')
                    elif i < len(s): return
                return bt(i, ip)

                
            if len(ip[-1]) < 3 and int(ip[-1] + s[i]) < 256:
                bak = ip[:]
                ip[-1] += s[i]
                bt(i+1, ip)
                ip = bak[:]
                #print('r:',i, ip)
                
            if len(ip) < 4 and (4 - len(ip)) <= len(s) - i <= (4 - len(ip)) * 3:
                #print('r:',i, ip)
                ip.append('')
                bt(i, ip)
            
        bt()
        return r