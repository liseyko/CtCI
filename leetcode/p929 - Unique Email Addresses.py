class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        realEmails = set()
        for email in emails:
            uf_name, domain = email.split('@')
            real_name = ''.join(uf_name.split('+')[0].split('.'))
            realEmails.add('@'.join([real_name, domain]))

        return len(realEmails)
