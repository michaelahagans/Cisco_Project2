import dns.resolver
import logging

logger = logging.getLogger()
logging.basicConfig(filename='logs.log',
                    format='%(lineno)s %(asctime)s %(filename)s: %(message)s', filemode='w')
#logging.basicConfig(filename='logs.log', format='%(levelname)s: %(message)s', filemode='w')
logger.setLevel(logging.DEBUG)


class Operations:

    def __init__(self, dns_record, record_type):
        self.dns_record = dns_record
        self.record_type = record_type

    def query(self):
        """ queries dns """
        answers = dns.resolver.resolve(self.dns_record, self.record_type)
        for answer in answers:
            print(answer)
        logger.info(
            f'DNS Query made for: {self.dns_record} Type: {self.record_type}')

    def add_record(self):
        print('Adding Records not yet supported.')
        logger.info('Adding Records not yet supported.')

    def update_record(self):
        print('Updating Records not yet supported.')
        logger.info('Updating Records not yet supported.')


if __name__ == '__main__':
    print('Follow the prompts to search, add or edit a DNS record')
    workflow = input('What would you like to do? (query, add, update): ')
    if workflow == 'query':
        dns_record = input('Enter the record to resolve: ')
        record_type = input('Enter the type of record (A, MX, PTR): ')
        try:
            ops = Operations(dns_record, record_type)
            query = ops.query()
        except Exception as err:
            logger.warning(f'Error occurred resolving your record: {err}')
    elif workflow == 'add':
        dns_record = input('Enter the record to add: ')
        record_type = input('Enter the type of record (A, MX, PTR): ')
        try:
            ops = Operations(dns_record, record_type)
            query = ops.add_record()
        except Exception as err:
            logger.warning(f'Error occurred adding your record: {err}')
    elif workflow == 'update':
        dns_record = input('Enter the record to update: ')
        record_type = input('Enter the type of record (A, MX, PTR): ')
        try:
            ops = Operations(dns_record, record_type)
            query = ops.update_record()
        except Exception as err:
            logger.warning(f'Error occurred adding your record: {err}')
    else:
        print('Unrecognized operation. Please try again.')
    print('Script complete')

