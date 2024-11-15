
<strong>🐺 Werewolf Game Server & Client</strong><br><br>
A multiplayer game application based on the classic <strong>"Werewolf: The Party Game."</strong>, implemented in Python. The project uses socket communication for a client-server setup and supports various player roles.

<br>
👥 Available Roles

<ul> <li><strong>Werewolf (`wolf`)</strong>: Can choose to eliminate a player during the night.</li> <li><strong>Seer (`seer`)</strong>: Can discover the role of another player.</li> <li><strong>Medium (`medium`)</strong>: Can learn the role of a dead player.</li> <li><strong>Chavalry (`chavalry`)</strong>: Can save a player from a werewolf attack.</li> <li><strong>Villager (`villager`)</strong>: Participates in the daytime vote to eliminate suspects.</li> </ul> <br>
🛠 Technologies Used

<ul> <li><strong>Python</strong>: Main programming language.</li> <li><strong>Socket</strong>: Used for client-server communication.</li> <li><strong>Threading</strong>: To manage multiple connections and concurrent actions.</li> <li><strong>JSON</strong>: For data transfer between client and server.</li> </ul> <br>
🚀 Features

<ul> <li>Multiplayer game supporting up to 10 players.</li> <li>Random role assignment for players.</li> <li>Automated game phases: <strong>night</strong> (role actions) and <strong>day</strong> (discussion and voting).</li> <li>Action resolution and event handling based on player roles.</li> <li>Automatic victory condition check (villagers vs. wolves).</li> </ul> <br> <br> 🤝 Contributing <br> Contributions, issues, and pull requests are welcome! Feel free to enhance the project and suggest new features.<br> <p align="center"> Made with ❤️ by <a href="https://github.com/DanielKirash">DanielKirash</a> </p>
