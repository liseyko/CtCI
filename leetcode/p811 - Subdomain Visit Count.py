class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = {}
        for rec in cpdomains:
            cnt, fqdn = rec.split()
            fqdn = fqdn.split('.')
            for i in range(len(fqdn)):
                d = '.'.join(fqdn[~i:])
                try:
                    res[d] += int(cnt)
                except:
                    res[d] = int(cnt)

        return [str(v)+" "+k for k, v in res.items()]
