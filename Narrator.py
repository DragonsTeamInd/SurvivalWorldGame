class Narrator():
    def __init__(self):
        self.voice = Sound('Sounds/',-1,80)
        self.images = ['','','']
        self.texts = ['ertyuiuytre','wertyhvcdf','sazdxfcgv']
        self.index = 0
    def textplay(self):
        for txt in self.texts:
            Text = txt
            TextFont = pygame.font.SysFont('None', 20)
            txt = TextFont.render(Text, 0, (255,255,255))
    def play_text_on_window(self,txtind,screen):
        if int(txtind) = txtind:
            screen.blit(self.texts[txtind],(0,0))
    def play_narrators_lore(self):
        play = True
        txtind = 0
        while play:
            if pressed_keys[K_SPACE]:
                play = False
            self.play_text_on_window(txtind,screen)
            AnimPlay(self,self.images,10)
            pygame.display.flip()
            txtind += 0.10
