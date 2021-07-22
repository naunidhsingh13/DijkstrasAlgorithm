
class UnionClass:

    def __init__(self, label, rank=1, parent=None):
        self.label = label
        self.rank = rank
        self.parent = parent if parent is not None else label


class UnionSet:

    def __init__(self, labels):
        self.labels = dict()
        for label in labels:
            self.labels[label] = UnionClass(label)

    @staticmethod
    def _find_parent_(obj_label):
        while obj_label.parent != obj_label.label:
            obj_label = obj_label.parent
        return obj_label

    def find_set(self, class_label):
        return self._find_parent_(self.labels[class_label]).label if class_label in self.labels else None

    def union(self, class_label_1, class_label_2):
        if class_label_1 > class_label_2:
            class_label_1, class_label_2 = class_label_2, class_label_1

        if class_label_1 not in self.labels or class_label_2 not in self.labels:
            return False

        obj_label1 = self._find_parent_(self.labels[class_label_1])
        obj_label2 = self._find_parent_(self.labels[class_label_2])

        if obj_label1 == obj_label2:
            return False

        if obj_label1.rank >= obj_label2.rank:
            obj_label2.parent = obj_label1
            obj_label1.rank += obj_label2.rank

        elif obj_label1.rank < obj_label2.rank:
            obj_label1.parent = obj_label2
            obj_label2.rank += obj_label1.rank

        return True