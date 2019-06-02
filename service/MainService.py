from service.DescriptionService import DescriptionService
from service.ImageService import ImageService


class MainService:

    def __init__(self):
        self.description_service = DescriptionService()
        self.image_service = ImageService()

    def compare_images(self, img_list1, img_list2):
        if len(img_list1) >= 3 and len(img_list2) >= 3:
            minim_similar_images = 3
        else:
            minim_similar_images = min(len(img_list1), len(img_list2))

        similar_images = 0

        for img1 in img_list1:
            for img2 in img_list2:
                if self.image_service.compare_images(img1, img2):
                    similar_images = similar_images + 1
            if similar_images == 0:
                break

        if similar_images < minim_similar_images:
            return False
        else:
            return True

    def compare_descriptions(self, description_info1, description_info2):
        same_info = 0

        for key, value in description_info1.items():
            if value is not None:
                if value == description_info2[key]:
                    same_info = same_info + 1
        if same_info / len(description_info1.keys()) >= 0.50:
            return True
        else:
            return False

    def is_same_announcement(self, img_list1, img_list2, description1, description2):
        description_info1 = self.description_service.get_description_info(description1)
        description_info2 = self.description_service.get_description_info(description2)

        if self.compare_descriptions(description_info1, description_info2):
            if self.compare_images(img_list1, img_list2):
                return True
            else:
                return False
        else:
            return False
