class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        for log in logs:
            print(log.split()[1])
