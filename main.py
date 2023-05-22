import os
import discord
from discord.ext import tasks
from itertools import cycle
from time import time
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("Pruz0/VescGPT")
model = AutoModelForCausalLM.from_pretrained("Pruz0/VescGPT")

tokenizerLen = AutoTokenizer.from_pretrained("Pruz0/LennGPT")
modelLen = AutoModelForCausalLM.from_pretrained("Pruz0/LennGPT")

tokenizerHaL = AutoTokenizer.from_pretrained("Pruz0/HaLLGPT")
modelHaL = AutoModelForCausalLM.from_pretrained("Pruz0/HaLLGPT")

tokenizerGeo = AutoTokenizer.from_pretrained("Pruz0/GeoGPT")
modelGeo = AutoModelForCausalLM.from_pretrained("Pruz0/GeoGPT")

tokenizerPruz = AutoTokenizer.from_pretrained("Pruz0/PruzGPT")
modelPruz = AutoModelForCausalLM.from_pretrained("Pruz0/PruzGPT")

managers = ['373913573153570827', '261784527318417411', '390414090813571082']

async def ask_vescgptlocal(inpp: str):
    t = time()
    print(f'Generating reply for: "{inpp}"')
      # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(tokenizer.eos_token + inpp, return_tensors='pt')
    # print(new_user_input_ids)

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if False else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(
        bot_input_ids, max_length=200,
        pad_token_id=tokenizer.eos_token_id,  
        no_repeat_ngram_size=3,       
        do_sample=True, 
        top_k=50, 
        top_p=0.7,
        temperature=1
    )
    
    # pretty print last ouput tokens from bot
    print(f'Response generated in {"%.3f" %(- t + time())} second(s)\n')
    return("{}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))

async def ask_lenngptlocal(inpp: str):
    t = time()
    print(f'Generating reply for: "{inpp}"')
      # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizerLen.encode(tokenizerLen.eos_token + inpp, return_tensors='pt')
    # print(new_user_input_ids)

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if False else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = modelLen.generate(
        bot_input_ids, max_length=200,
        pad_token_id=tokenizerLen.eos_token_id,  
        no_repeat_ngram_size=3,       
        do_sample=True, 
        top_k=50, 
        top_p=0.7,
        temperature=1
    )
    
    # pretty print last ouput tokens from bot
    print(f'Response generated in {- t + time()} second(s)\n')
    return("{}".format(tokenizerLen.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))


async def ask_hallgptlocal(inpp: str):
    t = time()
    print(f'Generating reply for: "{inpp}"')
      # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizerHaL.encode(tokenizerHaL.eos_token + inpp, return_tensors='pt')
    # print(new_user_input_ids)

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if False else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = modelHaL.generate(
        bot_input_ids, max_length=200,
        pad_token_id=tokenizerHaL.eos_token_id,  
        no_repeat_ngram_size=3,       
        do_sample=True, 
        top_k=50, 
        top_p=0.7,
        temperature=1
    )
    
    # pretty print last ouput tokens from bot
    print(f'Response generated in {"%.3f" %(- t + time())} second(s)\n')
    return("{}".format(tokenizerHaL.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))

async def ask_geogptlocal(inpp: str):
    t = time()
    print(f'Generating reply for: "{inpp}"')
      # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizerGeo.encode(tokenizerGeo.eos_token + inpp, return_tensors='pt')
    # print(new_user_input_ids)

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if False else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = modelGeo.generate(
        bot_input_ids, max_length=200,
        pad_token_id=tokenizerGeo.eos_token_id,  
        no_repeat_ngram_size=3,       
        do_sample=True, 
        top_k=50, 
        top_p=0.7,
        temperature=1
    )
    
    # pretty print last ouput tokens from bot
    print(f'Response generated in {"%.3f" %(- t + time())} second(s)\n')
    return("{}".format(tokenizerGeo.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))

async def ask_Pruzgptlocal(inpp: str):
    t = time()
    print(f'Generating reply for: "{inpp}"')
      # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizerPruz.encode(tokenizerPruz.eos_token + inpp, return_tensors='pt')
    # print(new_user_input_ids)

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if False else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = modelPruz.generate(
        bot_input_ids, max_length=200,
        pad_token_id=tokenizerPruz.eos_token_id,  
        no_repeat_ngram_size=3,       
        do_sample=True, 
        top_k=50, 
        top_p=0.7,
        temperature=1
    )
    
    # pretty print last ouput tokens from bot
    print(f'Response generated in {"%.3f" %(- t + time())} second(s)\n')
    return("{}".format(tokenizerPruz.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))

def main():
  return "Your Bot Is Ready"

status = cycle(['at CutawayShot Games', '?help'])

async def send_message(message, user_message, is_private):
  try:
    response_msg = ''
    gptName = ''

    prefixes = [',', '-', '$', '!', '+', 'start_conv']
    containsPrefix = False

    for p in prefixes:
      if user_message.startswith(p):
        containsPrefix = True
        break

    if not containsPrefix:
      return

    if user_message.startswith('start_conv'):
      vescSays = message.content[10:]
      response_msg += ('Vesco: ' + vescSays + '\n' + 'Lenny: ')

      lennSays = await ask_lenngptlocal(vescSays)
      response_msg += (lennSays + '\n' + 'Hall: ')
      hallSays = await ask_hallgptlocal(lennSays)
      response_msg += (hallSays + '\n' + 'Geo: ')
      geoSays = await ask_geogptlocal(hallSays)
      response_msg += (geoSays + '\n' + 'Pruz: ')
      pruzSays = await ask_Pruzgptlocal(geoSays)
      response_msg += (pruzSays + '\n' + 'Vesco: ')
      vescSays = await ask_vescgptlocal(pruzSays)
      response_msg += (vescSays + '\n' + 'Lenny: ')

      for l in range(5):
        lennSays = await ask_lenngptlocal(vescSays)
        response_msg += (lennSays + '\n' + 'Hall: ')
        hallSays = await ask_hallgptlocal(lennSays)
        response_msg += (hallSays + '\n' + 'Geo: ')
        geoSays = await ask_geogptlocal(hallSays)
        response_msg += (geoSays + '\n' + 'Pruz: ')
        pruzSays = await ask_Pruzgptlocal(geoSays)
        response_msg += (pruzSays + '\n' + 'Vesco: ')
        vescSays = await ask_vescgptlocal(pruzSays)
        response_msg += (vescSays + '\n' + 'Lenny: ')

      lennSays = await ask_lenngptlocal(vescSays)
      response_msg += lennSays

      gptName = "Pralk conversation"
    else:
    #message.content
      async with message.channel.typing():
        if user_message.startswith(','):
          response_msg = await ask_vescgptlocal(message.content[1:])
          gptName = 'Vescito'
        elif user_message.startswith('-'):
          response_msg = await ask_lenngptlocal(message.content[1:])
          gptName = 'Lenny'
        elif user_message.startswith('$'):
          response_msg = await ask_hallgptlocal(message.content[1:])
          gptName = 'HaLL'
        elif user_message.startswith('!'):
          response_msg = await ask_geogptlocal(message.content[1:])
          gptName = 'Geo'
        elif user_message.startswith('+'):
          response_msg = await ask_Pruzgptlocal(message.content[1:])
          gptName = 'Pruz'

        print(response_msg)

    is_private = False

    if response_msg == '' or gptName == '':
      return

    if is_private:
      await message.author.send(response_msg, delete_after=12)
    else:
      await message.reply(f'{gptName}:\n``{response_msg}``')

  except Exception as ex:
    print(ex)


def run_discord_bot():
  data_file = open("Bot_Data.pruz", "r")
  Token = data_file.read()
  data_file.close()

  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)

  @client.event
  async def on_ready():
    change_status.start()
    print('Bot is up and running.')

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if os.environ['asking'] == "True":
      await message.reply("Busy")
      return

    await send_message(message, str(message.content).lower(), True)

  @tasks.loop(seconds=10)
  async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

  client.run(Token)


if __name__ == '__main__':
  os.environ['asking'] = "False"
  run_discord_bot()
