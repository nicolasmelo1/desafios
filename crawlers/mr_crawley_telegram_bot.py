from telegram.ext import Updater, CommandHandler
from mr_crawley import MrCrawley


def start(bot, update):
    update.message.reply_text('''
Olá {}!

Para começar a usar o bot é muito simples, apenas mande /nadaprafazer para ver o que está bombando nos reddits de sua escolha. Ex.: /nadaprafazer cats;worldnews;dogs
    '''.format(update.message.from_user.first_name))


def help(bot, update):
    print('testeee')
    update.message.reply_text('Mande /nadaprafazer para ver o que está bombando nos reddits de sua escolha. Ex.: /nadaprafazer cats;worldnews;dogs')


def mine(bot, update, args):
    update.message.reply_text('Aguarde..')
    try:
        crawler = MrCrawley()
        subreddits = args[0].split(';')
        response = ''
        result = '''
Titúlo: {0}
Upvotes: {1}
Subreddit: {2}
Comentários: {3}
Thread: {4}
'''
        for subreddit in subreddits:
            crawler_response = crawler.whats_poppin(subreddit)
            for data in crawler_response:
                response = response + result.format(data['title'], data['upvotes'], data['subreddit'], data['comments'],
                                          data['thread'])

        update.message.reply_text(response)
    except (IndexError, ValueError):
        update.message.reply_text('Ex.: /nadaprafazer cats;worldnews;dogs')


updater = Updater('754605694:AAEuWdhs-ZTeqhdQBfmCj04-jb_dEUHdVxk')

dispatch = updater.dispatcher

dispatch.add_handler(CommandHandler('start', start))
dispatch.add_handler(CommandHandler('help', help))
dispatch.add_handler(CommandHandler('nadaprafazer', mine, pass_args=True))

updater.start_polling()
print('Bot Started')

updater.idle()