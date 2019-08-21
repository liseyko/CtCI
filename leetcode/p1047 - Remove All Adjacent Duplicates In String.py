class Solution:
    def removeDuplicates(self, S: str) -> str:
        st, i = [None], 0
        while i < len(S):
            if S[i] == st[-1]:
                st.pop()
            else:
                st.append(S[i])
            i += 1
        return ''.join(st[1:])
