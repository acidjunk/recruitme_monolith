from factory.django import DjangoModelFactory


class DeveloperFactory(DjangoModelFactory):

    class Meta:
        model = 'developers.Developer'

    # @Factory.post_generation
    # def skill_objects(self, create, extracted, **kwargs):
    #     if not create:
    #         # Simple build, do nothing.
    #         return
    #
    #     if extracted:
    #         # A list of groups were passed in, use them
    #         for skill_object in extracted:
    #             self.skill_objects.add(skill_object)


# class RecruiterFactory(DjangoModelFactory):
#
#     class Meta:
#         model = 'recruiters.Recruiter'


class SiteTreeFactory(DjangoModelFactory):

    class Meta:
        model = 'sitetree.Tree'


class SiteTreeItemFactory(DjangoModelFactory):

    class Meta:
        model = 'sitetree.TreeItem'


