# <strong>🐺 Werewolf Game Server & Client</strong><br><br>
Un'applicazione di gioco multiplayer basata sul classico <strong>"Lupi Mannari di Thiercelieux"</strong>, implementata in Python. Il progetto utilizza socket per la comunicazione client-server e supporta diversi ruoli per i giocatori.

<br>
👥 Ruoli disponibili
<ul> <li><strong>Lupo Mannaro (`wolf`)</strong>: Può scegliere di eliminare un giocatore durante la notte.</li> <li><strong>Veggente (`seer`)</strong>: Può scoprire il ruolo di un altro giocatore.</li> <li><strong>Medium (`medium`)</strong>: Può sapere il ruolo di un giocatore morto.</li> <li><strong>Cavaliere (`chavalry`)</strong>: Può salvare un giocatore dall'attacco dei lupi.</li> <li><strong>Villager (`villager`)</strong>: Contribuisce alla votazione diurna per eliminare i sospetti.</li> </ul> <br>
🛠 Tecnologie utilizzate
<ul> <li><strong>Python</strong>: Linguaggio di programmazione principale.</li> <li><strong>Socket</strong>: Utilizzato per la comunicazione client-server.</li> <li><strong>Threading</strong>: Per gestire connessioni multiple e azioni simultanee.</li> <li><strong>JSON</strong>: Per il trasferimento di dati tra client e server.</li> </ul> <br>
🚀 Caratteristiche
<ul> <li>Gioco multiplayer con supporto per 10 giocatori.</li> <li>Assegnazione casuale dei ruoli ai giocatori.</li> <li>Fasi di gioco automatizzate: <strong>notte</strong> (azioni dei ruoli) e <strong>giorno</strong> (discussione e votazione).</li> <li>Risoluzione delle azioni dei ruoli e gestione degli eventi di gioco.</li> <li>Verifica automatica delle condizioni di vittoria (villagers vs wolves).</li> </ul> <br>

<br>
🤝 Contribuire <br>
Contributi, issue e richieste di pull sono benvenuti! Sentiti libero di migliorare il progetto e di proporre nuove funzionalità.<br>

<p align="center"> Made with ❤️ by <a href="https://github.com/DanielKirash">DanielKirash</a> </p>
