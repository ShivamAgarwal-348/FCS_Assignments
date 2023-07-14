// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9; 

// importing the libraries
import "@openzeppelin/contracts@4.8.0/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts@4.8.0/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts@4.8.0/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts@4.8.0/access/Ownable.sol";
import "@openzeppelin/contracts@4.8.0/utils/Counters.sol";

contract FCS_NFT is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable { 
    // Our contract is inheriting from ERC721, ERC721Enumerable, ERC721URIStorage and Ownable
    // ownable prevent other users from using the smart contact to mint NFTs

    using Counters for Counters.Counter; // initialising counter to keep track of our NFTs

    Counters.Counter private _tokenIdCounter;

    constructor() ERC721("FCS_NFT", "FCS") {} // give name and symbol to your contract name : "FCS_NFT" , symbol : "FCS"

    function safeMint(address to, string memory uri) public onlyOwner { // to mint/ add a new entry on the blockchain
        // we need the address of the wallet with which we want to mint/deploy the NFT and uri is way to identify the metadata of your NFT
        // public : so that people can access the contract not just the smart contract
        // onlyOwner : so that only the wallet that deployed this smart contract can mint NFTs

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
    }

    // The following functions are overrides required by Solidity.

    function _beforeTokenTransfer(address from, address to, uint256 tokenId, uint256 batchSize)
        internal 
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId, batchSize);
    }

    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)// returns the uri of your token/NFT using the token id as input/parameter
        public
        view // function is only reading from the blockchain so we dont need to pay gas for it 
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
