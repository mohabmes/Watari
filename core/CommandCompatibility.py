from . import Utils


class CommandCompatibility:

    def check(self, sent, target = []):
        for keyword in target:

            keyword = keyword.lower()
            sent = sent.lower()

            if Utils.MED(keyword, sent) < 4:
                return True

        return False

