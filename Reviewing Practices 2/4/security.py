import re


class Security:

    def secure(self, info):
        parts = re.split('[\s,]+', info)
        for part in parts:
            if self.is_social_account_info(part):
                p = part.split('/')
                info = info.replace(part, ''.join([p[0], '/', self.encrypt(p[1])]))
        return info

    def is_social_account_info(self, param):
        r = re.match('[A-Z][a-z]*:www.[a-z]+.[a-z]+/[\w_]+', param)
        if r is None:
            return False
        return r.end() - r.start() == len(param)

    def encrypt(self, s):
        result = []
        parts = Security.split_to_uniforms(s)
        for part in parts:
            for j, char in enumerate(part):
                result.append(str((ord(char) - 96) * (j + 1)))
        return ''.join(result)

    @staticmethod
    def split_to_uniforms(s):
        parts = []
        j = 0
        i = 0
        for i in range(len(s)):
            if s[i] != s[j]:
                parts.append(s[j:i])
                j = i
        i += 1
        parts.append(s[j:i])
        return parts
