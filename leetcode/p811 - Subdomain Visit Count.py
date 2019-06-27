class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = collections.defaultdict(int)
        for record in cpdomains:
            cnt, fqdn = record.split()
            cnt = int(cnt)
            dl = fqdn.split('.')
            for i in range(1, len(dl)+1):
                d = '.'.join(dl[-i:])
                res[d] += cnt

        return [str(v)+' '+k for k, v in res.items()]
