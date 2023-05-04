confirm_Template_message = TemplateSendMessage(
    alt_text = '問你小問題',
    template = ConfirmTemplate(
        text = 'ARE YOU SURE?',
        actions = [
            PostBackAction(
                label = 'LIKE',
                display_text = 'REALLY LIKE',
                data = 'action = DO NOT REALLY LIKE'
            ),
            PostBackAction(
                label = 'BAD',
                display_text = 'NOT REALLY BAD',
                data = 'SUPER BAD'
            )
        ]
    )
)