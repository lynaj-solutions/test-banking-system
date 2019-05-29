import random
import factory
import logging
from faker import Faker
from django.contrib.auth.models import Group

from apps.profiles.choices import *

from apps.nOSClient.models import *
from apps.nOSUSer.models import *
from apps.poll.models import *

# from tests.seed.providers.ModelOfParticularPersonProviders.LanguagesModelProvider import *

from random import seed
from random import randint

logger = logging.getLogger(__name__)

faker = Faker()

faker.add_provider(LanguagesModelProvider)
faker.add_provider(CategoriesModelProvider)
faker.add_provider(StatsInfoModelProvider)

seed(1)

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(
    	lambda n: faker.user_name()
	)
    password = faker.password()
    email = factory.LazyAttribute(
    	lambda _: faker.email()
	)

class ModelOfParticularPersonFactory(factory.DjangoModelFactory):
	class Meta:
		model = ModelOfParticularPerson

	user = factory.SubFactory(UserFactory)
	email_address = factory.LazyAttribute(lambda _: faker.email())
	description = faker.text()
	instagramURL = faker.first_name_female()
	snapchatURL = faker.first_name_female()
	pornhubURL = faker.first_name_female()
	twitterURL = faker.first_name_female()
	freeonesURL = faker.first_name_female()
	xvideosURL = faker.first_name_female()
	amazonWishListURL = faker.first_name_female()
	paymentAddress = '0x8D4b8Cf94f40199f2d2c8173e4f6Bb1Cf8bA21EA'
	has_been_activated = True
	private_snapchatURL = faker.first_name_female()
	private_instagramURL = faker.first_name_female()

	@factory.post_generation
	def fillingStatsInfoModel(self, create, extracted, **kwargs):
		info_hair = faker.info_hair()
		info_orientation = faker.info_orientation()
		info_country = faker.info_country()
		info_weight = random.randint(1, 100)
		info_height = random.randint(1, 100)

		@factory.post_generation
		def adding_manytomany_field(self, create, extracted, **kwargs):
			queried_stats_info_model = StatsInfoModel.objects.filter(owner=
				self)
			self.info_languages.add(factory.SubFactory(LanguageModelFactory))
			self.info_categories.add(factory.SubFactory(CategoriesModelFactory))
			self.nickname = self.user.username
			self.save()

class LanguageModelFactory(factory.DjangoModelFactory):
	class Meta:
		model = LanguagesModel

	info_language = faker.info_language()

class CategoriesModelFactory(factory.DjangoModelFactory):
	class Meta:
		model = CategoriesModel

	category = faker.category()

class StatsInfoModelFactory(factory.DjangoModelFactory):
	class Meta:
		model = StatsInfoModel

	owner = factory.SubFactory(ModelOfParticularPersonFactory)
	info_hair = faker.info_hair()
	info_orientation = faker.info_orientation()
	info_country = faker.info_country()
	info_weight = random.randint(1, 100)
	info_height = random.randint(1, 100)

	@factory.post_generation
	def adding_manytomany_field(self, create, extracted, **kwargs):
		self.info_languages.add(factory.SubFactory(LanguageModelFactory))
		self.info_categories.add(factory.SubFactory(CategoriesModelFactory))