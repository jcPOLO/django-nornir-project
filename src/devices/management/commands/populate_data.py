from django.core.management.base import BaseCommand
from devices.models import Device, ModelType, Platform, Site
from menu.models import Template, Jinja2Template
import csv
import ipaddress
import datetime
import os


class Command(BaseCommand):

    @staticmethod
    def get_platforms(path='templates/jinja2'):
        try:
            return os.listdir(path)
        except Exception as e:
            raise e

    @staticmethod
    def get_jinja2_name(platform):
        path = f'templates/jinja2/{platform}'
        try:
            return os.listdir(path)
        except Exception as e:
            raise e

    @staticmethod
    def get_jinja2(platform, template):
        path = f'templates/jinja2/{platform}/'
        filename = ''.join(template)
        file = path + filename
        try:
            with open(file) as f:
                output = f.readlines()
            return ''.join(output)
        except Exception as e:
            return ''

    @staticmethod
    def is_ip(string: str) -> bool:
        try:
            ipaddress.ip_address(string)
            return True
        except ValueError:
            return False

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str,
                            help='The csv file that contains the inventory')

    def handle(self, *args, **kwargs):

        result = {}
        platforms = self.get_platforms()
        file_name = kwargs['file_name']

        site_obj = Site.objects.get_or_create(
            name='LaOnce',
            address='C/ Buena Vista 11 9º B',
            site_code='9999',
            phone='976713573'
        )

        with open(f'{file_name}.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                hostname = row[0] if self.is_ip(row[0]) else None
                host = row[4].replace(" ", "_") or None
                platform = row[2].lower().replace(" ", "_") if row[2].lower().replace(
                    " ", "_") in platforms else None
                model = row[6].replace(" ", "_") or None
                serial = row[7].replace(" ", "_") or None

                is_telnet = 't' in row[1].lower() and 's' not in row[1].lower()
                is_ssh = 's' in row[1].lower()

                # remove duplicated hostnames
                if None not in (hostname, host, platform) and host not in result.keys():
                    result[host] = {
                        'hostname': hostname,
                        'platform': platform,
                        'groups': [
                            'ios_telnet' if is_telnet and platform == 'ios' else platform
                        ],
                        'data': {
                            'site_code': '',
                            'model': model,
                            'serial': serial,
                            'role': {}
                        }

                    }
                    if is_telnet and platform == 'ios':
                        result[host]['port'] = 23

                    platform_obj = Platform.objects.get_or_create(
                        name=platform
                    )

                    model_type_obj = ModelType.objects.get_or_create(
                        name=model,
                        platform=platform_obj[0]
                    )

                    device_obj = Device.objects.get_or_create(
                        hostname=host,
                        ip_address=hostname,
                        platform=Platform.objects.get(name=platform),
                        serial=serial,
                        is_telnet=is_telnet,
                        is_ssh=is_ssh,
                        role='NA',
                        site=site_obj[0],
                    )
                    device_obj[0].model_type.add(model_type_obj[0])

                    device_obj[0].save()

        for platform in platforms:
            name_list = self.get_jinja2_name(platform)
            print('Platform:', platform)
            print('Name_list:', name_list)
            platform_obj = Platform.objects.get_or_create(name=platform)

            for name in name_list:
                print('Name y platform:', name, platform)
                config = self.get_jinja2(platform, name)
                if name:
                    template_obj = Template.objects.get_or_create(
                        name=name,
                        title='a modificar',
                    )
                if config:
                    template_obj[0].platform.add(platform_obj[0])
                    jinja2_template_obj = Jinja2Template.objects.get_or_create(
                        config=config,
                        platform=platform_obj[0],
                        template=template_obj[0]
                    )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
