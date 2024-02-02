import logging

from django.core.management.base import BaseCommand

from server.models import Model, Price, Provider

logger = logging.getLogger(__name__)

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete Address instances")
    Model.objects.all().delete()
    Price.objects.all().delete()
    Provider.objects.all().delete()


def create_model(
        name,
        size,
        developer,
        price_factor
):
    logger.info("Creating model")

    model = Model(
        name=name,
        developer=developer,
        size=size,
        price_factor=price_factor
    )
    model.save()
    logger.info("{} model created.".format(model))
    return model


def create_provider(
        name,
        url,
        pricing_url,
        pricing_tag_type,
        pricing_tag_name
):
    logger.info("Creating provider")

    provider = Provider(
        name=name,
        url=url,
        pricing_url=pricing_url,
        pricing_tag_type=pricing_tag_type,
        pricing_tag_name=pricing_tag_name
    )
    provider.save()
    logger.info("{} provider created.".format(provider))
    return provider


def create_price(
        price,
        provider,
        model
):
    logger.info("Creating price")

    price = Price(
        price=price,
        provider=provider,
        model=model
    )
    price.save()
    logger.info("{} price created.".format(price))
    return price


def run_seed(mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # TODO Create providers
    provider_openai = create_provider(
        name='OpenAI',
        url='https://openai.com/',
        pricing_url='https://openai.com/pricing',
        pricing_tag_type='div',
        pricing_tag_name='ui-blocks ui-blocks--padded'
    )
