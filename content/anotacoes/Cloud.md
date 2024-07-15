---
title: "Cloud"
date: 2023-08-15
lastmod: 2023-08-15
---
## [Cloud]({{< ref "Cloud" >}}) vs On Premises
> No último mês a Lambda3 saiu de uma infra on premises pra outra 100% nuvem. Desligamos uma estrutura com 2 servidores físicos de dez anos de idade (redundância) que tinham quase 200GB de RAM cada, diversos switches, firewall e cancelamos um link dedicado de 2 mil reais. Tínhamos umas dez VMs rodando.
> É uma infra pequena, mas adequada pras nossas necessidades. Temos um ADDS com 2 DCs, servidores de build, log, aplicação, firewall e outras coisinhas. Boa parte dos serviços já rodavam na nuvem, suíte de escritório no Microsoft 365, app no Azure app service, DevOps no Azure DevOps entre outros.
> Consolidamos alguns servidores. Os DCs rodam em VMs série B, custam 80 reais por mês cada. Sua demanda é mínima, pq usamos Azure AD pra praticamente tudo (e estamos vendo de sair do AD e ficar só no AAD, diminuindo ainda mais os custos).
> O custo no Azure: menos de 4 mil por mês (mas ainda estou apurando, talvez seja 20 a 30% menor que isso).
> O custo pra fazer um collocation com a exata infra que tínhamos (cotamos diversos fornecedores): de 7 a 12 mil reais por mês, e com alguns adicionais eventuais (por exemplo, para acessar fisicamente a máquina, a gente ou terceiros do próprio host, há custo).
> Minha conclusão é que a nuvem faz sentido pra empresas pequenas que não querem manter servidores. Mas... (e esse "mas" é importante) se a empresa tiver alguém pra manter os servidores (e vai precisar, mesmo se usar a nuvem), uma infra on premises ainda é muito mais barata.
> Pra vocês terem uma ideia, um dos servidores (ambos eram Dell) nós compramos mais de dez anos atrás. A única coisa que fizemos foi adicionar RAM e trocar discos (mecânicos) quando falharam. Novo, um desses custa uns dez mil reais. Mas fica melhor que isso. O outro servidor nós compramos usado, na região da Santa Efigenia em São Paulo, de uma empresa que compra máquinas que estão sendo substituídas de grandes empresas, e revende no varejo. Por dez mil você compra uma máquina bem poderosa, de 5 ou 8 anos atrás, e que vai rodar sem falhar por mais dez anos fácil. Essas máquinas não param.
> Dez mil reais, dois servidores, por dez anos, custa meros 166 reais por mês. Ok, coloca mais 2 de 5 mil reais, pra usar de firewall com OpnSense ou PFSense (redundância), dá 250 reais por mês.
> O custo maior vai estar no link, já que os provedores residenciais não entregam nenhuma qualidade. A gente usava fibra de uma grande operadora de SP, e dava problema toda hora, e a impressão que dá é que eles fazem de propósito pq você está usando muito. Só quando trocamos pra um dedicado de apenas 50mbps isso resolveu, mas custava 2 mil reais, mas havia links profissionais mais baratos, por cerca de mil reais. Então, 1.250 reais, mais o custo da energia e eventualmente alguma troca de HD/SSD a cada X anos.
> Nenhuma cloud ganha dessa eficiência. Mas você tem que saber operar.
> 
> Mudamos por outros motivos, se fosse por custo manteríamos nossa infra velhinha por mais dez anos.
> 
> Fora que na cloud você tem algumas limitações. Por exemplo, SMTP relay é proibido em toda grande cloud, pra evitar farms de spam, então você é obrigado a contratar um provedor de e-mail. E banda de Internet é sempre muito cara quando comparada com alternativas fora da cloud.
> 
> Ou seja, fiquem atentas(os), porque depende. Mas é bom ter isso em mente.
>
>
> Giovanni Bassi on https://twitter.com/giovannibassi/status/1656710931575980038

