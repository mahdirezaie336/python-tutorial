import re


class Security:

    def secure(self, info):
        result = []
        parts = re.split('[\s,]+', info)
        for part in parts:
            print(part)
            if self.is_social_account_info(part):
                p = part.split('/')
                result.append(p[0] + '/' + self.encrypt(p[1]))
            else:
                result.append(part)
            result.append(', ')
        del result[-1]
        return ''.join(result)

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


ss = Security()
print(ss.secure('FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02 Gender:male Instagram:www.instagram.com/aalavi Degree:Master Twitter:www.twiter.com/alaviii imdb:www.imdb.com/alavi'))
print(ss.is_social_account_info('Instagram:www.instagram.com/aalavi'))
