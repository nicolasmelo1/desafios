from telegram.ext import Updater, CommandHandler
from mr_crawley import MrCrawley


class TelegramBot:
    def __init__(self, key=None):
        self.minimum_score = None
        self.updater = Updater(key if key else '754605694:AAEuWdhs-ZTeqhdQBfmCj04-jb_dEUHdVxk')

        dispatch = self.updater.dispatcher

        dispatch.add_handler(CommandHandler('start', self.__start))
        dispatch.add_handler(CommandHandler('help', self.__help))
        dispatch.add_handler(CommandHandler('config', self.__config, pass_args=True))
        dispatch.add_handler(CommandHandler('nadaprafazer', self.__mine, pass_args=True))

        self.updater.start_polling()
        print('Bot Started')

        self.updater.idle()

    def __start(self, bot, update):
        """
        Runs on /start
        """
        update.message.reply_text('Olá {}! \nPara começar a usar o bot é muito simples, '
                                  'apenas mande /nadaprafazer para ver o que está '
                                  'bombando nos reddits de sua escolha. \n'
                                  'Ex.: /nadaprafazer cats;worldnews;dogs \n'
                                  'Caso deseja, você pode visualuzar a página principal'
                                  ' do reddit através do \'reddit_home\'\n'
                                  'Ex.: /nadaprafazer reddit_home \n'
                                  'Se estiver com dúvidas use /help'.format(update.message.from_user.first_name))

    def __help(self, bot, update):
        """
        Runs on /help -  retrieve commands for user and usage examples
        """
        update.message.reply_text('Mande /nadaprafazer para ver o que está '
                                  'bombando nos subreddits de sua escolha. '
                                  'Ex.: /nadaprafazer cats;worldnews;dogs \n'
                                  'Para configurar o numero minimo de upvotes de cada thread: /config ')

    def __config(self, bot, update, args):
        """
        Runs on /config - configure minumum number of upvotes to retrieve thread
        """

        if args:
            try:
                self.minimum_score = int(args[0])
                update.message.reply_text('Número minimo de upvotes alterado para: {}'.format(args[0]))
            except:
                update.message.reply_text('Insira um número. Ex.: /config 10000')
        else:
            update.message.reply_text('Insira um número. Ex.: /config 10000')

    def __mine(self, bot, update, args):
        """
        Runs on /nadaprafazer - retrieve threads that's poppin on reddit or subreddits
        """

        update.message.reply_text('Aguarde...')
        try:
            crawler = MrCrawley()
            response = crawler.mine(args[0].lower(), self.minimum_score if self.minimum_score else 5000)
            response = response.split('\n    \n')
            if len(response) > 5:
                for i in range(0, len(response), 5):
                    update.message.reply_text('\n    \n'.join(response[i:i+5]))
            else:
                update.message.reply_text('\n    \n'.join(response))
        except (IndexError, ValueError):
            update.message.reply_text('Ops!! \nAlguma coisa deu errado. '
                                      'Tente novamente como no exemplo: \n'
                                      '/nadaprafazer cats;worldnews;dogs')

