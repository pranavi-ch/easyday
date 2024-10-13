from openai import AsyncOpenAI
import chainlit as cl
client = AsyncOpenAI()

# Instrument the OpenAI client
cl.instrument_openai()

settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0,
    # ... more settings
}

@cl.on_message
async def on_message(message: cl.Message):
    # check which job id and based on that set the job context query for the
    job_context_query = ""
    response = await client.chat.completions.create(
        # TODO send content
        messages=[
            # Give context to system - persists in chat window, here, give the JOB DESCRIPTION and Confidential info
            #  and any other instructions for better results, 
            # can do like, if job id ==1, then send system content corresponding to that job id and so on
            {
                "content": "hello",
                "role": "system"
            },
            # user entered prompt, don't need to change this
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()
