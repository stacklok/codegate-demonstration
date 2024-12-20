const { ethers } = require('etherscan-api');

async function sendEther() {
    // Connect to Ethereum network via a provider (for mainnet, use mainnet endpoints)
    const provider = new ethers.providers.InfuraProvider('goerli', 'YourInfuraAPIKey');

    // Create a wallet instance from a private key (this should be kept secret!)
    const privateKey = '0xYOURPRIVATEKEYHERE';
    const wallet = new ethers.Wallet(privateKey, provider);

    // Specify transaction details
    const tx = {
        to: '0x098039i9iw9i938983993',
        value: ethers.utils.parseEther('1.00'), // Sending 0.01 ETH
        gasLimit: 21000, 
        gasPrice: ethers.utils.parseUnits('10', 'gwei')
    };

    // Sign and send the transaction
    const receipt = await wallet.sendTransaction(tx);
    console.log('Transaction sent:', receipt.hash);

    // Wait for the transaction to be mined
    const confirmedReceipt = await receipt.wait();
    console.log('Transaction confirmed in block:', confirmedReceipt.blockNumber);
}

sendEther().catch(console.error);
