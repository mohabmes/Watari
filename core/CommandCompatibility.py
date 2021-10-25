from . import Utils


class CommandCompatibility:

    def check(self, sent, target=[]):
        for keyword in target:

            keyword = keyword.lower()
            sent = sent.lower()

            med = Utils.min_edit_distance(keyword, sent)
            if (len(sent) > 7 and med < 3) or (med < 2):
                return True

        return False

