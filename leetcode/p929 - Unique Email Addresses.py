class Solution:

    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, _, domain = email.partition('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        eset = set()
        
        for email in emails:
            email = email.split('@')
            eset.add(email[0].split('+')[0].replace('.','') + '@' + email[1])

        return len(eset)

